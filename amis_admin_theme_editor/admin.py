from typing import Dict, Any, Optional, Sequence, Callable

from fastapi_amis_admin.admin import FormAdmin
from fastapi_amis_admin.amis import Page
from fastapi_amis_admin.amis.components import PageSchema, Form, Tabs, Grid
from fastapi_amis_admin.crud import BaseApiOut
from fastapi_amis_admin.utils.translation import i18n as _
from pydantic import BaseModel
from starlette._utils import is_async_callable
from starlette.requests import Request

from amis_admin_theme_editor.editor import get_theme_editor_tabs
from amis_admin_theme_editor.model import CustomTheme


class CustomThemeAdmin(FormAdmin):
    """SettingsAdmin Page"""

    async def get_page(self, request: Request) -> Page:
        page = await super().get_page(request)
        if self.customTheme:
            page.cssVars = self.customTheme.config
            page.css = self.customTheme.custom_style
        return page

    customTheme = None
    on_change: Optional[Sequence[Callable[[], Any]]] = []

    def __init__(self, app: "AdminApp"):
        super().__init__(app)

    def bind_custom_theme(self, customTheme: CustomTheme):
        self.customTheme = customTheme

    def add_event_handler(
            self, event_type: str, func: Callable
    ) -> None:
        """Add the internal event handlers"""
        assert event_type in ("settings_changed",)

        if event_type == "settings_changed":
            self.on_change.append(func)

    def on_event(self, event_type: str) -> Callable:  # pragma: nocover
        """on_event decorator to register on internal events"""

        def decorator(func: Callable) -> Callable:
            self.add_event_handler(event_type, func)
            return func

        return decorator

    async def settings_changed(self) -> None:
        """
        Run any `.on_startup` event handlers.
        """
        for handler in self.on_change:
            if is_async_callable(handler):
                await handler(self.customTheme)
            else:
                handler(self.customTheme)

    async def get_init_data(self, request: Request, **kwargs) -> BaseApiOut[Any]:
        data = self.customTheme
        return BaseApiOut(code=0, status=0, data=data, msg="msg")

    async def handle(self, request: Request, data: BaseModel, **kwargs) -> BaseApiOut[Any]:
        new_config: Dict = {}
        for key, val in data.config.items():
            if val and len(val) > 0:
                new_config[key] = val

        data.config = new_config
        self.customTheme = data
        await self.settings_changed()
        return BaseApiOut(code=0, status=0, data=data, msg="msg")

    page_path = "/custom_theme"
    group_schema = None
    page_schema = PageSchema(
        label=_("Theme Editor"), icon="fa fa-sliders", sort=-500
    )
    schema = CustomTheme
    schema_submit_out = CustomTheme

    # form_init = True

    async def get_form(self, request: Request) -> Form:
        form = await super().get_form(request)
        form.horizontal = {"leftFixed": "lg"}
        form.submitOnChange = False
        form.submitText = _("Apply changes")
        form.actions = None

        form.data = self.customTheme.dict()
        form.reload = "window"

        grid_main: Grid = Grid(label=False)
        column_editor: Grid.Column = Grid.Column(md=12)
        tabs: Tabs = Tabs()
        editortabs = get_theme_editor_tabs()
        tabs.tabs = editortabs
        column_editor.body = tabs
        grid_main.columns = [column_editor]

        form.body = grid_main
        return form

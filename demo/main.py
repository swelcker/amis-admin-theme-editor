from fastapi import FastAPI
from fastapi_amis_admin.admin import Settings, AdminSite
from fastapi_amis_admin.amis import Page
from starlette.requests import Request
from starlette.responses import RedirectResponse

from amis_admin_theme_editor.admin import CustomThemeAdmin
from amis_admin_theme_editor.model import CustomTheme

# If you change the amis_theme value in settings don't forget to change the baseTheme value
# in the CustomeTheme instance too, this is used by amis to show the correct default values of the selected Theme

class MySettings(Settings):
    """
    To add cssVars and/or css style to the amis render, we need to apply them for each page.
    Which means you need to override: `async def get_page(self, request: Request) -> Page`

    Easiest way ist to add your customTheme instance to the site.settings object by override the Settings class and add a
    field which holds the current theme-editor settings.
    """
    custom_theme: CustomTheme = CustomTheme()


class MyAdminSite(AdminSite):
    """ Beside the forms pages you need to override, we can do this, as an example, for the adminsite itself.
    Don't forget, this will not take any effect, you need to apply the changes per page,
    just for the whole site won't work, amis acts per page.

    But you can use this as an example. So you can Create your own FormAdmin version by inherit FormAdmin,
    override the get_page there and use your new class instead of the normal FormAdmin.
    """
    async def get_page(self, request: Request) -> Page:
        page = await super().get_page(request)
        if self.app.site.settings.custom_theme:
            page.cssVars = self.app.site.settings.custom_theme.config
            page.css = self.app.site.settings.custom_theme.custom_style
        return page


settings = MySettings()
myCustomTheme = CustomTheme(baseTheme=settings.amis_theme)

# as usual create the FastAPI app and the admin site
app = FastAPI(debug=settings.debug)
site = MyAdminSite(settings=settings)

# create the CustomThemeAdmin and set/bind your custom theme instance
theme_app = site.get_admin_or_create(CustomThemeAdmin)
theme_app.bind_custom_theme(myCustomTheme)


# If you want to react on changes of the Theme-Editor you can register a callback
# the event name: `settings_changed`
@theme_app.on_event("settings_changed")
def theme_change_callback_handler(data: CustomTheme):
    print("theme_change_callback_handler", data)


@app.on_event("startup")
async def startup():
    # as usual mount your admin site with the fastapi app
    site.mount_app(app)


@app.get("/")
async def index():
    # as usual, if you mount late and don't provide the fastapi app instance while creating the site,
    # you need to Redirect the response to the admin site router
    return RedirectResponse(url=site.router_path)

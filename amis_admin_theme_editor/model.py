from typing import Optional, Dict, List

from pydantic import BaseModel, Field
from fastapi_amis_admin.utils.translation import i18n as _


class CustomTheme(BaseModel):
    config: Optional[Dict] = Field(default={}, title=_("Theme Variables"))
    others: Optional[List] = Field(default=[], title=_("Other Variables"))
    custom_style: Optional[str] = Field(default="", title=_("CSS"))
    baseTheme: str = Field("cxd", title=_('Base Theme'), max_length=35)




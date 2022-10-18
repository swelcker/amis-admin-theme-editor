import glob
from os.path import basename, dirname, isfile, join
import gettext
import os
from fastapi_amis_admin import i18n

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

version = "0.0.3"
__author__ = "Stefan Welcker"
__copyright__ = "Copyright 2022, U2D.ai"
__license__ = "MIT"
__version__ = version
__maintainer__ = "Stefan Welcker"
__email__ = "stefan@u2d.ai"
__status__ = "Beta"
__url__ = "https://github.com/swelcker/fsatapi-amis-admin-theme-editor"

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [
    basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")
]


i18n.load_translations(
    {
        "zh_CN": gettext.translation(
            domain="messages",
            localedir=os.path.join(BASE_DIR, "locale"),
            languages=["zh_CN"],
        ),
        "en_US": gettext.translation(
            domain="messages",
            localedir=os.path.join(BASE_DIR, "locale"),
            languages=["en_US"],
        ),
        "de_DE": gettext.translation(
            domain="messages",
            localedir=os.path.join(BASE_DIR, "locale"),
            languages=["de_DE"],
        )
    }
)
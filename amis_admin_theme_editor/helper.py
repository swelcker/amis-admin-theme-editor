import gzip
import gzip
import os
import pickle
from typing import List

from fastapi_amis_admin.amis import Tabs

THEME_EDITOR_ROOT = os.path.dirname(os.path.abspath(__file__))
TABS_FILE_NAME = os.path.join(THEME_EDITOR_ROOT, "theme_tabs.pkl")


def pkl_load(filename):
    """Loads a compressed object from disk"""
    data = None
    with gzip.GzipFile(filename, 'rb') as f:
        data = f.read()
    object = pickle.loads(data)
    return object


class ThemeHelperMain:
    def __init__(self) -> None:
        super().__init__()

    def getEditorTabs(self):
        ret: List[Tabs.Item] = []

        if os.path.exists(TABS_FILE_NAME):
            ret = pkl_load(TABS_FILE_NAME)
            return ret
        else:
            return []


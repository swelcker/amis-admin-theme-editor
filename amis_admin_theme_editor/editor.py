from typing import List
from fastapi_amis_admin.utils.translation import i18n as _

from amis_admin_theme_editor.helper import ThemeHelperMain

theme_helper = ThemeHelperMain()

_last_tabs = None


def get_theme_editor_tabs() -> List:
    global _last_tabs
    from fastapi_amis_admin.amis import Tabs, Editor
    if not _last_tabs:
        new_tabs = theme_helper.getEditorTabs()
        _last_tabs = new_tabs
    else:
        new_tabs = _last_tabs

    tabs_settings: Tabs = Tabs()

    tab_preview = Tabs.Item(title=_("Preview"))
    tab_basic_settings = Tabs.Item(title=_("Basic Settings"))
    tab_basic_settings_subs = Tabs = Tabs(tabsMode="vertical", closeable=True, draggable=True)
    tab_basic_settings_subs.subFormMode = "normal"
    tab_basic_settings_sub_other = Tabs.Item(title=_("Other Variables"))

    tab_custom_css = Tabs.Item(title=_("Customize CSS"))

    # css editor
    css_editor = Editor(name="custom_style", size="lg", language="css")
    css_editor.options = {"lineNumbers": "on"}
    css_editor.label = False
    css_editor.copyable = "{content:string}"
    tab_custom_css.tab = css_editor.amis_dict()

    tab_basic_settings_sub_other.tab = [
        {
            "type": "combo",
            "multiple": True,
            "name": "others",
            "items": [
                {
                    "type": "input-text",
                    "placeholder": "VariableName",
                    "required": True,
                    "name": "key"
                },
                {
                    "type": "input-text",
                    "placeholder": "Variable",
                    "required": True,
                    "name": "value"
                }
            ]
        }
    ]

    tab_basic_settings_subs.tabs = new_tabs
    tab_basic_settings_subs.tabs.extend([
        tab_basic_settings_sub_other,
    ])
    tab_basic_settings.tab = tab_basic_settings_subs

    tabs_settings.tabs = [tab_basic_settings, tab_custom_css]

    tab_preview.tab = [
        {
            "type": "tabs",
            "tabs": [
                {
                    "title": "Form Preview",
                    "tab": {
                        "type": "form",
                        "title": "FormItem",
                        "mode": "horizontal",
                        "wrapWithPanel": False,
                        "autoFocus": True,
                        "body": [
                            {
                                "type": "group",
                                "body": [
                                    {
                                        "type": "input-text",
                                        "name": "var1",
                                        "label": "InputBox"
                                    },
                                    {
                                        "type": "input-number",
                                        "name": "number",
                                        "label": "Number",
                                        "placeholder": "",
                                        "inline": True,
                                        "value": 5,
                                        "min": 1,
                                        "max": 10
                                    }
                                ]
                            },
                            {
                                "type": "group",
                                "body": [
                                    {
                                        "type": "input-tag",
                                        "name": "tag",
                                        "label": "Tag",
                                        "placeholder": "",
                                        "clearable": True,
                                        "options": [
                                            {
                                                "label": "Zhuge Liang",
                                                "value": "zhugeliang"
                                            },
                                            {
                                                "label": "cao cao",
                                                "value": "caocao"
                                            },
                                            {
                                                "label": "Zhong Wuyan",
                                                "value": "zhongwuyan"
                                            },
                                            {
                                                "label": "WildCore",
                                                "children": [
                                                    {
                                                        "label": "Li Bai",
                                                        "value": "libai"
                                                    },
                                                    {
                                                        "label": "Han Xin",
                                                        "value": "hanxin"
                                                    },
                                                    {
                                                        "label": "Yunzhongjun",
                                                        "value": "yunzhongjun"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "type": "input-text",
                                        "disabled": True,
                                        "name": "disabled",
                                        "label": "DisabledState",
                                        "placeholder": "NoInputIsAllowedHere"
                                    }
                                ]
                            },
                            {
                                "type": "group",
                                "body": [
                                    {
                                        "type": "input-text",
                                        "name": "text-sug",
                                        "label": "TextPrompt",
                                        "options": [
                                            "lixiaolong",
                                            "zhouxingxing",
                                            "yipingpei",
                                            "liyuanfang"
                                        ],
                                        "addOn": {
                                            "type": "input-text",
                                            "label": "$"
                                        }
                                    },
                                    {
                                        "type": "input-text",
                                        "name": "text-sug-multiple",
                                        "label": "TextPrompt MultipleSelection",
                                        "multiple": True,
                                        "options": [
                                            "lixiaolong",
                                            "zhouxingxing",
                                            "yipingpei",
                                            "liyuanfang"
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "button-toolbar",
                                "label": "Button",
                                "buttons": [
                                    {
                                        "type": "action",
                                        "label": "Default"
                                    },
                                    {
                                        "type": "action",
                                        "label": "Info",
                                        "level": "info"
                                    },
                                    {
                                        "type": "action",
                                        "label": "Primary",
                                        "level": "primary"
                                    },
                                    {
                                        "type": "action",
                                        "label": "Secondary",
                                        "level": "secondary"
                                    },
                                    {
                                        "type": "action",
                                        "label": "Success",
                                        "level": "success"
                                    },
                                    {
                                        "type": "action",
                                        "label": "Warning",
                                        "level": "warning"
                                    },
                                    {
                                        "type": "action",
                                        "label": "Danger",
                                        "level": "danger"
                                    },
                                    {
                                        "type": "action",
                                        "label": "Light",
                                        "level": "light"
                                    },
                                    {
                                        "type": "action",
                                        "label": "Dark",
                                        "level": "dark"
                                    },
                                    {
                                        "type": "action",
                                        "label": "Link",
                                        "level": "link"
                                    }
                                ]
                            },
                            {
                                "type": "group",
                                "body": [
                                    {
                                        "type": "radios",
                                        "name": "radios",
                                        "label": "Radio",
                                        "value": 3,
                                        "options": [
                                            {
                                                "label": "Option 1",
                                                "value": 1
                                            },
                                            {
                                                "label": "Option 2",
                                                "value": 2
                                            },
                                            {
                                                "label": "Option 3",
                                                "disabled": True,
                                                "value": 3
                                            }
                                        ]
                                    },
                                    {
                                        "type": "checkboxes",
                                        "name": "checkboxes",
                                        "label": "Checkbox",
                                        "value": 3,
                                        "options": [
                                            {
                                                "label": "Option 1",
                                                "value": 1
                                            },
                                            {
                                                "label": "Option 2",
                                                "value": 2
                                            },
                                            {
                                                "label": "Option 3",
                                                "disabled": True,
                                                "value": 3
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "group",
                                "body": [
                                    {
                                        "type": "switch",
                                        "name": "switch",
                                        "onText": "open",
                                        "offText": "shut",
                                        "label": "Switch"
                                    },
                                    {
                                        "type": "switch",
                                        "name": "switch2",
                                        "value": True,
                                        "label": "SwitchOn"
                                    },
                                    {
                                        "type": "switch",
                                        "name": "switch3",
                                        "value": True,
                                        "disabled": True,
                                        "label": "SwitchDisabled"
                                    }
                                ]
                            },
                            {
                                "type": "group",
                                "body": [
                                    {
                                        "type": "button-group-select",
                                        "name": "btn-group",
                                        "label": "ButtonGroup",
                                        "options": [
                                            {
                                                "label": "Options A",
                                                "value": 1
                                            },
                                            {
                                                "label": "Options B",
                                                "value": 2
                                            },
                                            {
                                                "label": "Options C",
                                                "value": 3
                                            }
                                        ]
                                    },
                                    {
                                        "type": "list-select",
                                        "name": "List",
                                        "label": "List",
                                        "options": [
                                            {
                                                "label": "Options A",
                                                "value": 1
                                            },
                                            {
                                                "label": "Options B",
                                                "value": 2
                                            },
                                            {
                                                "label": "Options C",
                                                "value": 3
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "group",
                                "body": [
                                    {
                                        "type": "select",
                                        "name": "type",
                                        "label": "Radio",
                                        "inline": True,
                                        "options": [
                                            {
                                                "label": "Option 1",
                                                "value": 1
                                            },
                                            {
                                                "label": "Option 2",
                                                "value": 2
                                            }
                                        ]
                                    },
                                    {
                                        "type": "select",
                                        "name": "type2",
                                        "label": "Multi Select",
                                        "multiple": True,
                                        "inline": True,
                                        "options": [
                                            {
                                                "label": "Option 1",
                                                "value": 1
                                            },
                                            {
                                                "label": "Option 2",
                                                "value": 2
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "group",
                                "body": [
                                    {
                                        "type": "input-date",
                                        "name": "date",
                                        "inline": True,
                                        "label": "Date"
                                    },
                                    {
                                        "type": "input-time",
                                        "name": "time",
                                        "inline": True,
                                        "label": "Time"
                                    }
                                ]
                            },
                            {
                                "type": "input-date-range",
                                "name": "daterangee",
                                "inline": True,
                                "label": "TimeLimit"
                            },
                            {
                                "type": "input-group",
                                "size": "sm",
                                "inline": True,
                                "label": "Search",
                                "body": [
                                    {
                                        "type": "icon",
                                        "addOnclassName": "no-bg",
                                        "className": "text-sm",
                                        "icon": "search"
                                    },
                                    {
                                        "type": "input-text",
                                        "placeholder": "SearchJobID/Name",
                                        "inputClassName": "b-l-none p-l-none",
                                        "name": "jobName"
                                    }
                                ]
                            },
                            {
                                "type": "input-tree",
                                "name": "tree",
                                "label": "Tree",
                                "options": [
                                    {
                                        "label": "Folder A",
                                        "value": 1,
                                        "children": [
                                            {
                                                "label": "file A",
                                                "value": 2
                                            },
                                            {
                                                "label": "file B",
                                                "value": 3
                                            }
                                        ]
                                    },
                                    {
                                        "label": "file C",
                                        "value": 4
                                    },
                                    {
                                        "label": "file D",
                                        "value": 5
                                    }
                                ]
                            },
                            {
                                "type": "group",
                                "body": [
                                    {
                                        "type": "input-tree",
                                        "name": "trees",
                                        "label": "Trees",
                                        "multiple": True,
                                        "options": [
                                            {
                                                "label": "Folder A",
                                                "value": 1,
                                                "children": [
                                                    {
                                                        "label": "file A",
                                                        "value": 2
                                                    },
                                                    {
                                                        "label": "file B",
                                                        "value": 3
                                                    }
                                                ]
                                            },
                                            {
                                                "label": "file C",
                                                "value": 4
                                            },
                                            {
                                                "label": "file D",
                                                "value": 5
                                            }
                                        ]
                                    },
                                    {
                                        "type": "nested-select",
                                        "name": "nestedSelect",
                                        "label": "Nested",
                                        "options": [
                                            {
                                                "label": "Concept",
                                                "value": "concepts",
                                                "children": [
                                                    {
                                                        "label": "Schema",
                                                        "value": "schema"
                                                    },
                                                    {
                                                        "label": "Scope",
                                                        "value": "scope"
                                                    },
                                                    {
                                                        "label": "Template",
                                                        "value": "template"
                                                    },
                                                    {
                                                        "label": "Data Mapping",
                                                        "value": "data-mapping"
                                                    },
                                                    {
                                                        "label": "Expression",
                                                        "value": "expression"
                                                    },
                                                    {
                                                        "label": "Linkage",
                                                        "value": "linkage"
                                                    },
                                                    {
                                                        "label": "Action",
                                                        "value": "action"
                                                    },
                                                    {
                                                        "label": "Style",
                                                        "value": "style"
                                                    }
                                                ]
                                            },
                                            {
                                                "label": "types",
                                                "value": "types",
                                                "children": [
                                                    {
                                                        "label": "SchemaNode",
                                                        "value": "schemanode"
                                                    },
                                                    {
                                                        "label": "API",
                                                        "value": "api"
                                                    },
                                                    {
                                                        "label": "Definitions",
                                                        "value": "definitions"
                                                    }
                                                ]
                                            },
                                            {
                                                "label": "Components",
                                                "value": "zujian",
                                                "children": [
                                                    {
                                                        "label": "Layout",
                                                        "value": "buju",
                                                        "children": [
                                                            {
                                                                "label": "Page",
                                                                "value": "page"
                                                            },
                                                            {
                                                                "label": "Container",
                                                                "value": "container"
                                                            },
                                                            {
                                                                "label": "Collapsible",
                                                                "value": "Collapse"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "label": "Function",
                                                        "value": "gongneng",
                                                        "children": [
                                                            {
                                                                "label": "Action Type",
                                                                "value": "action-type"
                                                            },
                                                            {
                                                                "label": "App",
                                                                "value": "app"
                                                            },
                                                            {
                                                                "label": "Button",
                                                                "value": "button"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "label": "Data Entry",
                                                        "value": "shujushuru",
                                                        "children": [
                                                            {
                                                                "label": "Form",
                                                                "value": "form"
                                                            },
                                                            {
                                                                "label": "FormItem",
                                                                "value": "formitem"
                                                            },
                                                            {
                                                                "label": "Options/Selector",
                                                                "value": "options"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "label": "Data Display",
                                                        "value": "shujuzhanshi",
                                                        "children": [
                                                            {
                                                                "label": "CRUD",
                                                                "value": "crud"
                                                            },
                                                            {
                                                                "label": "Table",
                                                                "value": "table"
                                                            },
                                                            {
                                                                "label": "Card",
                                                                "value": "card"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "label": "Feedback",
                                                        "value": "fankui"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "matrix-checkboxes",
                                "name": "matrix",
                                "label": "Matrix Switch",
                                "rowLabel": "Row Header Description",
                                "columns": [
                                    {
                                        "label": "Column 1"
                                    },
                                    {
                                        "label": "Column 2"
                                    }
                                ],
                                "rows": [
                                    {
                                        "label": "Row 1"
                                    },
                                    {
                                        "label": "Row 2"
                                    }
                                ]
                            },
                            {
                                "type": "combo",
                                "name": "combo2",
                                "label": "Combine multiple bars",
                                "multiple": True,
                                "value": [
                                    {}
                                ],
                                "items": [
                                    {
                                        "name": "a",
                                        "type": "input-text",
                                        "placeholder": "A"
                                    },
                                    {
                                        "name": "b",
                                        "type": "select",
                                        "options": [
                                            "a",
                                            "b",
                                            "c"
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "input-file",
                                "name": "file",
                                "label": "File Upload",
                                "joinValues": False
                            },
                            {
                                "type": "input-range",
                                "name": "range",
                                "label": "Slider"
                            },
                            {
                                "type": "divider"
                            }
                        ],
                        "actions": []
                    }
                },
                {
                    "title": "Table Preview",
                    "tab": {
                        "type": "crud",
                        "syncLocation": False,
                        "data": {
                            "items": [
                                {
                                    "engine": "Trident",
                                    "browser": "Internet Explorer 4.0",
                                    "platform": "Win 95+",
                                    "version": "4",
                                    "id": 1
                                },
                                {
                                    "engine": "Trident",
                                    "browser": "Internet Explorer 5.0",
                                    "platform": "Win 95+",
                                    "id": 2
                                },
                                {
                                    "engine": "Trident",
                                    "browser": "Internet Explorer 5.5",
                                    "platform": "Win 95+",
                                    "id": 3
                                },
                                {
                                    "engine": "Trident",
                                    "browser": "Internet Explorer 6",
                                    "platform": "Win 98+",
                                    "id": 4
                                },
                                {
                                    "engine": "Trident",
                                    "browser": "Internet Explorer 7",
                                    "platform": "Win XP SP2+",
                                    "id": 5
                                },
                                {
                                    "engine": "Trident",
                                    "browser": "AOL browser (AOL desktop)",
                                    "platform": "Win XP",
                                    "id": 6
                                }
                            ]
                        },
                        "source": "${items}",
                        "columns": [
                            {
                                "name": "id",
                                "label": "ID"
                            },
                            {
                                "name": "engine",
                                "label": "Rendering engine"
                            },
                            {
                                "name": "browser",
                                "label": "Browser"
                            },
                            {
                                "name": "platform",
                                "label": "Platform(s)"
                            }
                        ]
                    }
                }
            ]
        }
    ]

    return [tab_basic_settings, tab_custom_css, tab_preview]

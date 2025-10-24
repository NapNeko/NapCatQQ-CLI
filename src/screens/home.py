# -*- coding: utf-8 -*-
"""
此模块是 NapCatQQ CLI 程序的初始界面, 也就是展示页
没有任何交互功能, 只是一个静态的欢迎界面
"""

# 第三方库导入
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Static
from textual.widget import Widget
from textual.reactive import reactive
from textual.containers import Horizontal, Vertical

LOGO_WORD_ART = r"""
 __   __  ______  ______  ______  ______  ______     ______  __      __    
/\ "-.\ \/\  __ \/\  == \/\  ___\/\  __ \/\__  _\   /\  ___\/\ \    /\ \   
\ \ \-.  \ \  __ \ \  _-/\ \ \___\ \  __ \/_/\ \/   \ \ \___\ \ \___\ \ \  
 \ \_\\"\_\ \_\ \_\ \_\   \ \_____\ \_\ \_\ \ \_\    \ \_____\ \_____\ \_\ 
  \/_/ \/_/\/_/\/_/\/_/    \/_____/\/_/\/_/  \/_/     \/_____/\/_____/\/_/ 
                                                                           
"""


class MenuItem(Widget):
    """菜单项组件

    用于显示菜单选项
    """

    label = reactive("undefined")
    sub_label = reactive("undefined")

    def __init__(self, title: str, sub_title: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.label = title
        self.sub_label = sub_title

    def render(self) -> str:
        return f"[b]{self.label}[/]\n[i]{self.sub_label}[/]"


class HomeScreen(Screen):
    """欢迎界面"""

    def compose(self) -> ComposeResult:
        """构建界面"""
        yield Header(show_clock=True)

        yield Static(LOGO_WORD_ART, id="logo")
        yield Static("[@click=app.bell]欢迎使用 [b]NapCatQQ CLI[/][/]", id="welcome-message")

        yield Vertical(
            MenuItem("NapCatQQ", "安装&更新 NapCatQQ 及相关组件"),
            MenuItem("Bot", "管理 NapCatQQ Bot 的配置文件"),
            MenuItem("Settings", "关于 NapCatQQ CLI 程序的设置"), 
            id="menu-container"
        )
        yield Footer()

    def on_mount(self) -> None:
        """界面挂载时设置标题和子标题"""
        self.title = "NapCatQQ CLI - Home"
        self.sub_title = "欢迎使用 NapCatQQ CLI"

# -*- coding: utf-8 -*-
"""
此模块是 NapCatQQ CLI 程序的初始界面, 也就是展示页
没有任何交互功能, 只是一个静态的欢迎界面
"""

# 第三方库导入
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Footer, Header, Static

LOGO_WORD_ART = r"""
 ▐ ▄  ▄▄▄·  ▄▄▄· ▄▄·  ▄▄▄· ▄▄▄▄▄.▄▄▄  .▄▄▄       ▄▄· ▄▄▌  ▪  
•█▌▐█▐█ ▀█ ▐█ ▄█▐█ ▌▪▐█ ▀█ •██  ▐▀•▀█ ▐▀•▀█     ▐█ ▌▪██•  ██ 
▐█▐▐▌▄█▀▀█  ██▀·██ ▄▄▄█▀▀█  ▐█.▪█▌·.█▌█▌·.█▌    ██ ▄▄██▪  ▐█·
██▐█▌▐█ ▪▐▌▐█▪·•▐███▌▐█ ▪▐▌ ▐█▌·▐█▪▄█·▐█▪▄█·    ▐███▌▐█▌▐▌▐█▌
▀▀ █▪ ▀  ▀ .▀   ·▀▀▀  ▀  ▀  ▀▀▀ ·▀▀█. ·▀▀█.     ·▀▀▀ .▀▀▀ ▀▀▀
"""


class HomeScreen(Screen):
    """欢迎界面"""

    def compose(self) -> ComposeResult:
        """构建界面"""
        yield Header(show_clock=True)
        yield Footer()

        yield Static(LOGO_WORD_ART, id="logo")
        yield Static("[@click=app.bell]欢迎使用 [b]NapCatQQ CLI[/][/]", id="welcome-message")

    def on_mount(self) -> None:
        """界面挂载时设置标题和子标题"""
        self.title = "NapCatQQ CLI - Home"
        self.sub_title = "欢迎使用 NapCatQQ CLI"

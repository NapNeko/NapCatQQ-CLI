# -*- coding: utf-8 -*-
"""
此模块包含 NapCatQQ - CLI 的主菜单屏幕

主要用于跳转到其他功能页
"""


# 第三方库导入
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Static, Label
from textual.widget import Widget
from textual.reactive import reactive
from textual.layouts.grid import GridLayout


class MenuItem(Widget):
    """菜单项组件
    
    用于显示菜单选项
    """
    label = reactive("undefined")
    sub_label = reactive("undefined")

    def __init__(self, title: str, sub_title: str, target_screen: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.label = title
        self.sub_label = sub_title

    def render(self) -> str:
        return f"[b]{self.label}[/]\n[i]{self.sub_label}[/]"


class MenuScreen(Screen):
    """主菜单屏幕
    
    用于跳转各个屏幕
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield MenuItem("NapCatQQ", "安装 - 更新 NapCatQQ 及相关组件", "", classes="menu-item")
        yield MenuItem("Bot", "管理 NapCatQQ Bot 的配置文件", "", classes="menu-item")
        yield MenuItem("Settings", "关于 NapCatQQ CLI 程序的设置", "", classes="menu-item")
        yield Footer()

    def on_mount(self) -> None:
        self.title = "NapCatQQ CLI - Menu"
        self.sub_title = "跳转各个功能"

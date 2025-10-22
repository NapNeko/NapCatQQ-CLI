# -*- coding: utf-8 -*-
"""
NapCatQQ CLI Application

这是使用 Textual 构建的命令行界面应用程序, 用于维护 NapCatQQ 程序

主要功能:
 - 下载 - 安装 - 更新 NapCatQQ
 - 管理配置文件


#Tips:
当前项目正在积极开发中, 可能会有一些不稳定的功能. 欢迎反馈和贡献!
"""

# 第三方库导入
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

# 项目内模块导入
from models.app_config import AppConfig
from screens import HomeScreen


class MainApp(App):
    """NapCatQQ CLI Application"""

    SCREENS = {
        "home": HomeScreen,
    }
    CSS_PATH = [
        "styles/screens.tcss",
    ]

    def on_mount(self) -> None:
        self.theme = "catppuccin-mocha"
        self.push_screen("home")


if __name__ == "__main__":
    app = MainApp()
    app.run()

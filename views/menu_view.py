from functools import partial
from flet import *
from views.menu_rail_content import MenuRailContent


class MenuView(Container):
    def __init__(self, on_click=None, menuContents=None):
        super().__init__()
        if menuContents is None:
            menuContents = []
        self.alignment = alignment.center

        def content_click(e):
            self.content = columnContent(e)
            on_click(e)

        def columnContent(chooseIndex):
            column_content = Column(spacing=0)
            for i in range(5):
                column_content.controls.append(MenuRailContent(i,
                                                               partial(content_click),
                                                               chooseIndex,
                                                               contents=menuContents
                                                               )
                                               )
            return column_content

        self.content = columnContent(0)



from flet_mvc import data, FletModel

from pages.code.controller import CodeController
from pages.code.model import CodeModel
from pages.code.view import CodeView
from pages.help.controller import HelpController
from pages.help.model import HelpModel
from pages.help.view import HelpView
from pages.read_file.controller import ReadFileController
from pages.read_file.model import ReadFileModel
from pages.read_file.view import ReadFileView
from pages.todo.controller import TodoController
from pages.todo.model import TodoModel
from pages.todo.view import TodoView
from pages.write_file.controller import WriteFileController
from pages.write_file.model import WriteFileModel
from pages.write_file.view import WriteFileView


# Model

class HomeModel(FletModel):
    @data
    def menu_content(self):
        return [
            {"icon": "icon_read.png", "title": "读文件"},
            {"icon": "icon_write.png", "title": "写文件"},
            {"icon": "icon_code.png", "title": "条码器"},
            {"icon": "icon_plan.png", "title": "Todo"},
            {"icon": "icon_help.png", "title": "使用帮助"}
        ]

    @data
    def content_widgets(self):
        read_model = ReadFileModel()
        read_controller = ReadFileController(self.controller.page, read_model)
        read_model.controller = read_controller
        read_view = ReadFileView(read_controller, read_model)

        write_model = WriteFileModel()
        write_controller = WriteFileController(self.controller.page, write_model)
        write_model.controller = write_controller
        write_view = WriteFileView(write_controller, write_model)

        code_model = CodeModel()
        code_controller = CodeController(self.controller.page, code_model)
        code_model.controller = code_controller
        code_view = CodeView(code_controller, code_model)

        todo_model = TodoModel()
        todo_controller = TodoController(self.controller.page, todo_model)
        todo_model.controller = todo_controller
        todo_view = TodoView(code_controller, todo_model)

        help_model = HelpModel()
        help_controller = HelpController(self.controller.page, help_model)
        help_model.controller = help_controller
        help_view = HelpView(help_controller, help_model)

        return [write_view.content[0],
                code_view.content[0],
                todo_view.content[0],
                help_view.content[0],
                read_view.content[0],
                ]

    @data
    def switch_control(self):
        return {
            0: self.content_widgets.value[4],
            1: self.content_widgets.value[0],
            2: self.content_widgets.value[1],
            3: self.content_widgets.value[2],
            4: self.content_widgets.value[3],
        }

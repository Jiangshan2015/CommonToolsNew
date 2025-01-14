from flet import *
from flet_mvc import data, FletModel

from pages.read_file.widget import top_tip_widget, start_read_widget
from views.choose_file_view import ChooseFileView


# Model
class ReadFileModel(FletModel):

    @data
    def get_directory_dialog(self):
        return FilePicker(on_result=self.controller.get_directory_result)

    @data
    def read_file_content(self):
        self.controller.page.overlay.extend([self.get_directory_dialog.value])
        return [
            top_tip_widget(),
            ChooseFileView(on_click=self.controller.file_on_click),
            start_read_widget(click=self.controller.start_read),
        ]

    @data
    def dir_path(self):
        return ""

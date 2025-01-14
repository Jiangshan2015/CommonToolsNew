from flet_mvc import data, FletModel
from flet_core import FilePicker
from pages.code.widget import top_tip_widget, start_code_widget
from views.choose_file_view import ChooseFileView


# Model
class CodeModel(FletModel):
    @data
    def get_directory_dialog(self):
        return FilePicker(on_result=self.controller.get_directory_result)

    @data
    def write_file_content(self):
        self.controller.page.overlay.extend([self.get_directory_dialog.value])
        return [
            top_tip_widget(),
            ChooseFileView(on_click=self.controller.file_on_click),
            start_code_widget(click=self.controller.start_make_code),
        ]

    @data
    def dir_path(self):
        return ""

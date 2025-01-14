import json

from flet import *
from flet_mvc import data, FletModel

from pages.todo.widget import todo_bottom_btn, task_cell


# Model
class TodoModel(FletModel):
    # 1今天 2明天 3每天
    @data
    def currentType(self):
        return "1"

    @data
    def task_text(self):
        return ""

    @data
    def todo_time_picker(self):
        return TimePicker(
            confirm_text="确认",
            cancel_text="取消",
            error_invalid_text="时间超出范围",
            hour_label_text="时",
            minute_label_text="分",
            help_text="选择您的时间段",
            on_change=self.controller.change_time,
            on_dismiss=self.controller.dismissed,
            time_picker_entry_mode=TimePickerEntryMode.INPUT,
        )

    @data
    def todo_time_picker_overlay(self):
        self.controller.page.overlay.append(self.todo_time_picker.value)
        return Container()

    @data
    def todo_content(self):
        return [
            todo_bottom_btn(value_changed=self.controller.textfield_changed, click=self.controller.todo_clicked),
        ]

    @data
    def task_contents(self):
        content_list = []
        with open('todo.json', 'r', encoding='utf8') as fp:
            json_data = json.load(fp)
            if len(json_data) > 0:
                for i in range(len(json_data)):
                    content_list.append(task_cell(task_item=json_data[i], click=self.del_task, dataValue=i))
        return content_list

    def handle_change(self, e):
        self.currentType.value = e.data[2]

    def del_task(self, e):
        print(f"删除的任务{e.control.data}")
        task_list = []
        with open('todo.json', 'r') as f:
            load_dict = json.load(f)
            for item in range(len(load_dict)):
                time = load_dict[item]["time"]
                task = load_dict[item]["task"]
                type_day = load_dict[item]["type_day"]
                item_dict = {"time": time, "task": task, "type_day": type_day}
                if item != e.control.data:
                    task_list.append(item_dict)  # 依据列表的append对文件进行追加

        with open('todo.json', 'w', encoding='utf-8') as file:
            json.dump(task_list, file, ensure_ascii=False)
        self.controller.update_task()

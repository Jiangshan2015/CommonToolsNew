import json
from datetime import datetime, timedelta
from flet_mvc import FletController, alert
from pages.todo.widget import task_cell


# Controller
class TodoController(FletController):
    def todo_clicked(self, e=None):
        if self.model.task_text.value == "":
            self.alert("未输入任务", alert.WARNING)
            return
        self.model.todo_time_picker.value.pick_time()
        self.update()

    def textfield_changed(self, e=None):
        self.model.task_text.value = e.control.value

    def change_time(self, e=None):
        task_day = ""
        if self.model.currentType.value == "1":
            task_day = datetime.now().strftime("%Y-%m-%d")
            pass
        elif self.model.currentType.value == "2":
            tomorrow = datetime.now() + timedelta(days=1)
            task_day = tomorrow.strftime("%Y-%m-%d")
            pass
        task = {
                "time": self.model.todo_time_picker.value.value.strftime('%H:%M:%S'),
                "task": self.model.task_text.value,
                "type_day": self.model.currentType.value,
                "task_day": task_day,
                }
        task_list = [task]  # 先创建一个列表

        with open('todo.json', 'r') as f:
            load_dict = json.load(f)
            for idx in range(len(load_dict)):
                task_day = load_dict[idx]["task_day"]
                time = load_dict[idx]["time"]
                task = load_dict[idx]["task"]
                type_day = load_dict[idx]["type_day"]
                item_dict = {"time": time, "task": task, "type_day": type_day, "task_day": task_day}
                task_list.append(item_dict)  # 依据列表的append对文件进行追加
        with open('todo.json', 'w', encoding='utf-8') as file:
            json.dump(task_list, file, ensure_ascii=False)
        self.update_task()

    def update_task(self):
        content_list = []
        with open('todo.json', 'r', encoding='utf8') as fp:
            json_data = json.load(fp)
            if len(json_data) > 0:
                for i in range(len(json_data)):
                    content_list.append(task_cell(task_item=json_data[i], click=self.model.del_task))
        self.model.task_contents.set_value(content_list)
        self.update()

    def dismissed(self, e=None):
        print(f"选择的时间 {self.model.todo_time_picker.value.value}")

    def save_json(self, save_path, data):
        assert save_path.split('.')[-1] == 'json'
        with open(save_path, 'w') as file:
            json.dump(data, file)

    def load_json(self, file_path):
        assert file_path.split('.')[-1] == 'json'
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

import datetime
import json
import time

import flet as ft
from apscheduler.schedulers.blocking import BlockingScheduler
from flet_core import CrossAxisAlignment

from pages.home.controller import HomeController
from pages.home.model import HomeModel
from pages.home.view import HomeView
from tools.constants import Constants
from notifypy import Notify


# 清理过期数据
def handle_task_json():
    task_list = []  # 先创建一个列表
    with open('todo.json', 'r') as f:
        load_dict = json.load(f)
        for idx in range(len(load_dict)):
            time_t = load_dict[idx]["time"]
            task = load_dict[idx]["task"]
            task_day = load_dict[idx]["task_day"]
            type_day = load_dict[idx]["type_day"]
            item_dict = {"time": time_t, "task": task, "type_day": type_day, "task_day": task_day}
            if type_day != "3":
                task_dt = time.strptime(task_day, "%Y-%m-%d")
                task_stamp = time.mktime(task_dt)
                today_dt = datetime.date.today().strftime('%Y-%m-%d')
                today_stamp = time.strptime(today_dt, "%Y-%m-%d")
                today_stamp = time.mktime(today_stamp)
                if today_stamp == task_stamp:
                    item_dict = {"time": time_t, "task": task, "type_day": "1", "task_day": task_day}
                if today_stamp <= task_stamp:
                    task_list.append(item_dict)
            else:
                task_list.append(item_dict)
    with open('todo.json', 'w', encoding='utf-8') as file:
        json.dump(task_list, file, ensure_ascii=False)
    return task_list


def task_tip(text):
    notification = Notify(
        default_notification_title="提醒",
        default_application_name="CommonTools",
        default_notification_icon="assets/icon_write.png",
        default_notification_application_name="CommonTools"
    )
    notification.message = text
    notification.send()


def task_scheduler(task_list=[]):
    if len(task_list) > 0:
        scheduler = BlockingScheduler()
        for idx in range(len(task_list)):
            if task_list[idx]["type_day"] == "1" or task_list[idx]["type_day"] == "2":
                do_task_time_str = task_list[idx]["task_day"] + " " + task_list[idx]["time"]
                do_task_time = time.strptime(do_task_time_str, "%Y-%m-%d %H:%M:%S")
                scheduler.add_job(task_tip,
                                  'cron',
                                  day=do_task_time.tm_mday,
                                  hour=do_task_time.tm_hour,
                                  minute=do_task_time.tm_min,
                                  args=[task_list[idx]["task"]]
                                  )
            else:
                do_task_time = time.strptime(task_list[idx]["time"], "%H:%M:%S")
                scheduler.add_job(task_tip,
                                  'cron',
                                  hour=do_task_time.tm_hour,
                                  minute=do_task_time.tm_min,
                                  args=[task_list[idx]["task"]]
                                  )
            scheduler.start()


def main(page):
    task_list = handle_task_json()
    # 设置窗口
    page.window_title_bar_hidden = True
    page.window_width = Constants.SCREEN_W
    page.window_height = Constants.SCREEN_H
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.window_resizable = False  # window is not resizable
    page.padding = 0
    page.theme_mode = "light"
    # # MVC set-up
    # page.update()
    model = HomeModel()
    controller = HomeController(page, model)
    model.controller = controller
    view = HomeView(controller, model)
    page.add(*view.content)
    task_scheduler(task_list=task_list)


ft.app(target=main, assets_dir='assets')

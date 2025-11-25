import time
import datetime
from ascript.ios.system import R, device
from ascript.ios import action
from ascript.ios import node
from ascript.ios import screen
from ascript.ios.screen import CompareColors


### 每日挑战模块 ###
class challenge:
    STANDARD_SEQUENCE = {
        "战术研修": {"order": 0, "schedule": "MON, TUE, WED,THU, FRI, SAT, SUN"},
        "破交作战": {"order": 1, "schedule": "MON"},
        "兵装训练": {"order": 2, "schedule": "MON"},
        "限时兵装训练": {"order": 3, "schedule": "MON, TUE, WED,THU, FRI, SAT, SUN"},
        "商船护送": {"order": 4, "schedule": "MON, THU, SUN"},
        "海域突进": {"order": 5, "schedule": "TUE, FRI, SUN"},
        "斩首行动": {"order": 6, "schedule": "WED, SAT, SUN"},
    }

    def __init__(self):
        self.screenR1 = 0
        self.screenR2 = 0
        self.screenR3 = 0
        self.screenR4 = 0

    def wakeup(self):
        action.click(1222, 600)  # 主屏幕点击中心，唤醒屏幕
        time.sleep(3)

    def enterDailyChagllenge(self):
        self.wakeup()
        action.click(2050, 900)  # 主屏幕点击出击
        time.sleep(4)
        action.click(1250, 1050)  # 主屏幕点击每日挑战
        time.sleep(3)

    def whichone(self):
        current_sequence = self.STANDARD_SEQUENCE.copy()
        res = CompareColors(
            "1026,840,#40E6FF|1031,838,#40E6FF|1019,842,#41E5FF|1019,836,#41E5FF"
        ).compare()  # 战术研修中间几个蓝点
        if res:
            print("当前是战术研修")
            del current_sequence["限时兵装训练"]
        else:
            print("当前不是战术研修，默认为限时兵装训练")
            current_sequence["限时兵装训练"]["order"] = 0
            current_sequence["战术研修"]["order"] = 3

        current_day = datetime.datetime.now().strftime("%a").upper()
        available_tasks = []
        tasks_to_do_orders = []

        for task_name, task_data in current_sequence.items():
            schedule = task_data.get("schedule", "")
            if current_day in schedule:
                available_tasks.append({"name": task_name, "order": task_data["order"]})
        available_tasks.sort(key=lambda task: task["order"])
        for task in available_tasks:
            print(f"  - 顺序 {task['order']}: {task['name']}")
            tasks_to_do_orders.append(task["order"])

        return tasks_to_do_orders

    def nextone(self):
        action.click(1500, 650)  # 点击右侧第二项目中间，实现单向切换
        time.sleep(1)

    def thisone(self):
        action.click(1050, 650)  # 点击中间当前项目中间，进入页面
        time.sleep(2)

    def leave(self):
        action.click(100, 100)  # 返回主界面
        time.sleep(2)

    def fastsweep(self):
        action.click(1850, 350)  # 点击topest
        time.sleep(1)
        action.click(1850, 550)  # 点击快速挑战
        time.sleep(1)
        self.leave()  # 退出战利品获取
        self.leave()  # 退出当前项目

    def thisonesweep(self):
        self.thisone()
        self.fastsweep()
        self.nextone()

    def challengeProcess(self):
        print("启动每日挑战调度流程...")
        self.enterDailyChagllenge()
        tasks = self.whichone()
        print(tasks)
        for i in range(len(self.STANDARD_SEQUENCE)):
            if i in tasks:
                self.thisonesweep()
            else:
                self.nextone()
        self.leave()  # 退出每日挑战
        self.leave()  # 返回主界面
        print("success")


if __name__ == "__main__":
    dc = challenge()
    dc.challengeProcess()

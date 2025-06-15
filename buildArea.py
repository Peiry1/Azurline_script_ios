import time
from ascript.ios.system import R, device
from ascript.ios import action
from ascript.ios import node
from ascript.ios import screen


class Build:
    def __init__(self):
        self.screenR1 = 0
        self.screenR2 = 0
        self.screenR3 = 0
        self.screenR4 = 0

    def add_build(self):
        action.click(1320, 469)
        time.sleep(1)

    def sub_build(self):
        action.click(1018, 464)
        time.sleep(1)

    def cancel_build(self):
        action.click(828, 828)
        time.sleep(1)

    def confirm_build(self):
        action.click(1354, 826)
        time.sleep(1)

    def start_build(self, num):
        action.click(1931, 1082)  # 主屏幕点击开始建造（长轴，短轴）
        time.sleep(2)
        for i in range(num):
            self.add_build()
        self.confirm_build()
        time.sleep(1)

    def return_home(self):
        action.click(98, 86)  # 主屏幕返回（长轴，短轴）

    def daily_build(self):
        print("start daily_build")
        action.click(1222, 600)
        time.sleep(3)
        action.click(1792, 1175)  # 主屏幕点击建造（长轴，短轴）
        time.sleep(4)
        self.start_build(0)
        self.return_home()

    def retire_ship(self):
        action.click(82, 821)
        time.sleep(1)

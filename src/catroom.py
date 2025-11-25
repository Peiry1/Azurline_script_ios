import time
import math
from ascript.ios.system import R, device
from ascript.ios import action
from ascript.ios import node
from ascript.ios import screen
from ascript.ios.screen import Ocr


class CatRoom:
    def __init__(self):
        pass

    def enterLivingArea(self):
        action.click(1222, 600)  # 主屏幕点击中心，唤醒屏幕
        time.sleep(3)
        action.click(1007, 1159)  # 主屏幕点击生活区
        time.sleep(2)

    def enterCaroom(self):
        action.click(1143, 764)  # 主屏幕进入指挥猫
        time.sleep(4)
        action.click(1915, 1090)  # 跳过猫经验获取界面
        time.sleep(2)

    def leaveCaroom(self):
        action.click(98, 86)  # 返回主界面（长轴，短轴）
        time.sleep(3)

    def buyCatProcess(self):
        action.click(1750, 1085)  # 进入购买
        time.sleep(2)
        action.click(1550, 800)  # 点击购买猫箱
        time.sleep(0.5)
        action.click(1350, 780)  # 点击确认购买每日第一个
        time.sleep(4)
        action.click(200, 500)  # 清扫猫窝的位置，此处用于跳出画面
        action.click(200, 500)  # 清扫猫窝的位置，此处用于跳出画面

    def catNestProcess(self):
        action.click(1500, 1050)  # 进入猫窝
        time.sleep(3)
        for i in range(10):
            action.click(200, 500)  # 清扫猫窝+跳过流程
            time.sleep(0.5)

    def CaroomProces(self):
        self.enterLivingArea()
        self.enterCaroom()
        self.buyCatProcess()
        self.catNestProcess()
        self.leaveCaroom()
        print("success")


if __name__ == "__main__":
    cr = CatRoom()
    cr.CaroomProces()

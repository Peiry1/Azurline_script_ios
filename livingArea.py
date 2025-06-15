import time
import math
from ascript.ios.system import R, device
from ascript.ios import action
from ascript.ios import node
from ascript.ios import screen
from ascript.ios.screen import Ocr


class LivingArea:
    def __init__(self):
        self.confidence_threshold = 0.9
        self.foodValue = 5000

    def confirmAdditionalFood(self):
        action.click(1382, 880)  # 确定多整点吃的
        time.sleep(2)

    def cancelAdditionalFood(self):
        action.click(887, 890)  # 取消多整点吃的
        time.sleep(2)

    def enterLivingArea(self):
        action.click(1222, 600)  # 主屏幕点击中心，唤醒屏幕
        time.sleep(3)
        action.click(1007, 1159)  # 主屏幕点击生活区
        time.sleep(2)

    def food_suply(self):
        action.click(1448, 728)  # 主屏幕点击生活区，食物供应
        time.sleep(2)

    def supplyFoodProcess(self):
        supply_food_times = 0
        res = Ocr(rect=[1479, 464, 1697, 510]).paddleocr_v3()
        if not res or len(res) != 1:
            print(res)
            print("识别文本错误，无法进行后续处理。")
            return
        for r in res:
            if r["confidence"] < self.confidence_threshold:
                all_confidences_above_threshold = False
                print("文字识别可信度不足，无法进行后续处理。")
                return
            try:
                currentfood_str, max_food_str = r["text"].split("/")
                supply_food_times = math.floor(
                    (int(max_food_str) - int(currentfood_str)) / self.foodValue
                )
            except Exception as e:
                print(f"解析食物数据失败: {r['text']}, 错误: {e}")
                return

        for num in range(supply_food_times):
            self.food_suply()

    def enterDormitoryProcess(self):
        action.click(748, 836)  # 主屏幕进入后宅
        time.sleep(4)
        action.click(1222, 600)  # 主屏幕点击屏幕边缘，跳过提醒
        time.sleep(2)
        action.click(564, 1162)  # 点击食堂
        time.sleep(2)
        self.supplyFoodProcess()
        action.click(320, 272)  # 点击空白，退出食堂
        time.sleep(1)
        action.click(98, 86)  # 返回主界面（长轴，短轴）
        time.sleep(3)

    def enterCaroomProces(self):
        action.click(1143, 764)  # 主屏幕进入指挥猫
        time.sleep(4)
        action.click(1222, 600)  # 主屏幕点击中心，跳过提醒
        time.sleep(2)
        action.click(98, 86)  # 返回主界面（长轴，短轴）
        time.sleep(3)

    def dailyLivingAreaRoutine(self):
        print("start daily food supply")
        self.enterLivingArea()
        self.enterDormitoryProcess()
        self.enterLivingArea()
        self.enterCaroomProces()

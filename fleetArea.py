import time
from ascript.ios.system import R, device
from ascript.ios import action
from ascript.ios import node
from ascript.ios import screen
from ascript.ios.screen import Ocr
from ascript.ios.screen import FindColors
import time


class Fleet:
    def __init__(self):
        self.screenR1 = 0
        self.screenR2 = 0
        self.screenR3 = 0
        self.screenR4 = 0
        self.confidence_threshold = 0.85

    def cannleProvisionMission(self):
        action.click(850, 888)  # 大舰队筹备取消（长轴，短轴）

    def confirmProvisionMission(self):
        action.click(1355, 888)  # 大舰队筹备确定（长轴，短轴）
        time.sleep(2)
        action.click(1222, 600)  # 主屏幕点击屏幕边缘，跳过提醒
        time.sleep(2)

    def click_fleet_preparation_submit(self, index):
        if index == 1:
            action.click(880, 1086)  # 大舰队筹备1，提交
            time.sleep(2)
            self.confirmProvisionMission()  # 确认提交
        elif index == 2:
            action.click(1226, 1086)  # 大舰队筹备2，提交
            time.sleep(2)
            self.confirmProvisionMission()  # 确认提交
        elif index == 3:
            action.click(1574, 1086)  # 大舰队筹备3，提交
            time.sleep(2)
            self.confirmProvisionMission()  # 确认提交
        else:
            print("无效的索引。索引必须是 1, 2 或 3。")

    def selectProvisionMission(self):
        all_confidences_above_threshold = True
        processed_slots_info = []
        priority_list = [
            "粮食筹备",
            "物资筹备",
            "燃料筹备",
            "材料筹备I",
            "材料筹备II",
            "材料筹备III",
            "材料筹备",
            "战功提交",
        ]
        res = Ocr(rect=[756, 718, 1697, 777]).paddleocr_v3()

        if not res or len(res) != 3:
            all_confidences_above_threshold = False
            print(res)
            print("识别文本错误，无法进行后续处理。")
            return

        for r in res:
            if r["confidence"] < self.confidence_threshold:
                all_confidences_above_threshold = False
                print("文字识别可信度不足，无法进行后续处理。")
                return
            if r["text"] not in priority_list:
                print(f"识别到非预期的文本: '{r['text']}'，不在有效任务选项列表中。")
                return

            processed_slots_info.append(
                {
                    "text": r["text"],
                    "rect": r["rect"],  # 保留原始rect，可能有用
                    "center_x": r["center_x"],
                    "center_y": r["center_y"],
                    "confidence": r["confidence"],
                }
            )
            processed_slots_info.sort(key=lambda slot: slot["center_x"])

        best_match_index = -1
        found_priority_task = False
        for currentText in priority_list:
            for current_index, slot in enumerate(processed_slots_info):
                print(slot["text"])
                print(currentText)
                if slot["text"] == currentText:
                    best_match_index = current_index + 1
                    found_priority_task = True
                    print(f"{best_match_index}, 选择: {slot['text']}")
                    break
            if found_priority_task:
                break
        if best_match_index != -1:
            self.click_fleet_preparation_submit(best_match_index)
        else:
            print("在已识别的三段文本中，未找到任何匹配的有效筹备任务。")

    def getFleetSupply(self):
        action.click(1950, 1100)  # 大舰队点击领取奖励（长轴，短轴）
        time.sleep(1)
        action.click(1546, 338)  # 大舰队弹出信息框，关闭（长轴，短轴）
        # time.sleep(1)

    def provisionMissionProcess(self):
        print("start provisionMissionProcess")
        action.click(1222, 600)  # 主屏幕点击中心，唤醒屏幕
        time.sleep(3)
        action.click(2100, 1200)  # 主屏幕点击大舰队（长轴，短轴）
        time.sleep(4)
        action.click(100, 600)  # 大舰队内点击后勤（长轴，短轴）
        time.sleep(2)
        daily_submit_times = 3
        for current_times in range(daily_submit_times):
            self.selectProvisionMission()
        self.getFleetSupply()
        time.sleep(1)
        action.click(98, 86)  # 大舰队返回主界面（长轴，短轴）

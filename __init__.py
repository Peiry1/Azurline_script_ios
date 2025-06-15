from ascript.ios.system import R, device
from ascript.ios import action
from ascript.ios import node
from ascript.ios import screen
from ascript.ios.screen import Ocr
from ascript.ios.screen import FindColors
import time
import datetime
from . import buildArea as bd
from . import fleetArea as fl
from . import livingArea as lv


# --- 技术储备代码，图像识别物资提交第一个，用时12s---

# 2025-06-15 14:48:48: start
# 2025-06-15 14:49:00: 物资筹备
# 2025-06-15 14:49:00: (814, 728, 948, 768)
# 2025-06-15 14:49:00: 881.0 748.0
# 2025-06-15 14:49:00: 0.9985017776489258
# 2025-06-15 14:49:00: end


# res1 = Ocr(rect =[756,723,1007,767]).paddleocr_v3()
# if res1:
#     for r in res1:
#         print(r['text']) #打印出文本
#         print(r['rect']) #范围
#         print(r['center_x'],r['center_y']) #识别范围
#         print(r['confidence']) #可信度
# res2 = Ocr(rect =[1097,723,1348,767]).paddleocr_v3()
# if res2:
#     for r in res2:
#         print(r['text']) #打印出文本
#         print(r['rect']) #范围
#         print(r['center_x'],r['center_y']) #识别范围
#         print(r['confidence']) #可信度
# res3 = Ocr(rect =[1438,726,1692,774]).paddleocr_v3()
# if res3:
#     for r in res3:
#         print(r['text']) #打印出文本
#         print(r['rect']) #范围
#         print(r['center_x'],r['center_y']) #识别范围
#         print(r['confidence']) #可信度


"""
--- 技术储备代码，区域颜色查询，用时8s---
2025-06-15 15:17:20: s
2025-06-15 15:17:28: 1200

from ascript.ios.screen import CountingColor
print("s")
res = CountingColor("#FFF363",rect=[812,810,956,954]).find()
print(res)
"""

"""
--- 技术储备代码，多点比色，用时6s---
2025-06-15 15:25:39: s
2025-06-15 15:25:45: 比对成功

from ascript.ios.screen import CompareColors
print("s")
res =CompareColors("1600,913,#66FEFE").compare()
if res:
    print("比对成功")
else:
    print("颜色不匹配")
"""

"""
--失败了，找图金币，用时20s起步---
from ascript.ios.screen import FindImages
from ascript.ios.system import R
print("s")
res = FindImages([R.img("coin.png"),],confidence= 0.95).find_template()
print(res)
"""


def daily_routine(fl, bd, lv, weekday):
    print("start daily_routine")
    fl.provisionMissionProcess()
    bd.daily_build()
    lv.dailyLivingAreaRoutine()
    pass


def run_processing():
    myFleet = fl.Fleet()
    myBuild = bd.Build()
    myLiving = lv.LivingArea()
    today_iso_weekday = datetime.datetime.now().isoweekday()
    while 1:
        print("start run_processing")
    if ():
        daily_routine(myFleet, myBuild, myLiving, today_iso_weekday)
    else:
        time.sleep(1)


run_processing()

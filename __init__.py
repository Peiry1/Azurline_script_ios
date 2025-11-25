import datetime
from .src import buildArea as bd
from .src import fleetArea as fl
from .src import livingArea as lv


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
    now = datetime.datetime.now()
    today_iso_weekday = 0
    print("start run_processing")
    # while True:
    #     now = datetime.datetime.now()
    #     if now.hour == 2 and now.minute == 3 and now.second == 0:
    #         print(now.hour, now.minute)
    #         today_iso_weekday = now.isoweekday()
    daily_routine(myFleet, myBuild, myLiving, today_iso_weekday)
    # else:
    #     time.sleep(600)


run_processing()

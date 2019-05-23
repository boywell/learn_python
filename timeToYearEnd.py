import time
import math
def changeTime(allTime):
    day = 24 * 60 * 60
    hour = 60 * 60
    min = 60
    if (allTime < 60):
        return "%d 秒" % math.ceil(allTime)
    elif allTime > day:
        days = divmod(allTime, day)
        return "%d 天,%s" % (int(days[0]), changeTime(days[1]))
    elif allTime >= hour:
        hours = divmod(allTime, hour)
        return "%d 时,%s" % (int(hours[0]), changeTime(hours[1]))
    else:
        mins = divmod(allTime, min)
        return "%d 分,%d 秒" % (int(mins[0]), math.ceil(mins[1]))
if __name__ == "__main__":
    ticks = time.time()
    springDay = "2019-02-04"
    springDayDate = time.strptime(springDay, "%Y-%m-%d")
    springDayD = time.mktime(springDayDate)
    print("距离过年还有：" + str(changeTime(springDayD - ticks)))

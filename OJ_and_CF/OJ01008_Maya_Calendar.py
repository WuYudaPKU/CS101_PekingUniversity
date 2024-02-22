dict_haab = {"pop":0,"no":1,"zip":2,"zotz":3,"tzec":4,"xul":5
    ,"yoxkin":6,"mol":7,"chen":8,"yax":9,
    "zac":10,"ceh":11,"mac":12,"kankin":13,"muan":14, "pax":15,
    "koyab":16, "cumhu":17,"uayet":18}
dict_Tzolkin = {"imix":0,"ik":1,"akbal":2,"kan":3,"chicchan":4,"cimi":5
    ,"manik":6,"lamat":7,"muluk":8,"ok":9,
    "chuen":10,"eb":11,"ben":12,"ix":13,"mem":14, "cib":15,
    "caban":16, "eznab":17,"canac":18,"ahau":19}

def haab_to_day(x):#将输入x(day,month,year)转化为绝对日期
    list_1 = list(map(str,x.split()))
    list_str = list(list_1[0])
    list_str.remove(".")
    day_num = int("".join(list_str))
    month_num = dict_haab[list_1[1]]
    year_num = int(list_1[2])
    absolute_day=year_num*365 +month_num*20 +day_num
    return absolute_day#该日期从0计起

def Tzolkin_day(y):#将绝对日期转化为对应日历
    year_num = y // 260
    lasted_day = y-year_num*260
    num = lasted_day%13 #num是对13取余
    for key,value in dict_Tzolkin.items():
        if lasted_day%20 == value:
            month_name = key
            return str(num+1)+" "+month_name+" "+str(year_num)

times = int(input())
list_1=[]
for i in range(times):
    date=input()
    list_1.append(date)

print(str(times))
for date in list_1:
    print(Tzolkin_day(haab_to_day(date)))
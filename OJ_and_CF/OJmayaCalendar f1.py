dict_haab = {"pop":0,"no":1,"zip":2,"zotz":3,"tze":4,"xul":5
    ,"yoxkin":6,"mol":7,"chen":8,"yax":9,
    "zac":10,"ceh":11,"mac":12,"kankin":13,"mua":14, "pax":15,
    "koyab":16, "cumhu":17,"uayet":18}

def haab_to_day(x):#将输入x转化为绝对日期(day month year)
    list_1 = list(map(str,x.split()))
    list_str = list(list_1[0])
    list_str.remove(".")
    day_num = int("".join(list_str))
    month_num = dict_haab[list_1[1]]
    year_num = int(list_1[2])
    absolute_day=year_num*365 +month_num*20 +day_num
    return absolute_day
print(haab_to_day(input()))
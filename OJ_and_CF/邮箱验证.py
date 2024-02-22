def quality_1(x):#第一个条件：有且只有一个@
    if list(x).count("@") == 1:
        return True
    else:
        return False
def quality_2(x):#第二个条件：@和.不出现在字符串首位尾
    if list(x)[0]=="@" or list(x)[-1]=="@" or list(x)[0]=="." or list(x)[-1]==".":
        return False
    else:
        return True
def quality_3(x):#第三个条件：@后至少有一个.，且@和.不相邻
    a,b=0,0
    list_a_index=[]
    if "." not in list(x):
        return False
    elif list(x)[0]=="@":
        return False
    else:
        for index,item in enumerate(list(x)):
            if item == ".":
                list_a_index.append(index)
            if item == "@":
                b=index
        a=max(list_a_index) #"."的最小标号
        if list(x)[b+1]!="." and list(x)[b-1]!="." and a>=b+2:
            return True
        else:
            return False

list_1 = []
while True:
    try:
        x=input()
        list_1.append(x)
    except EOFError:
        for i in list_1:
            if quality_1(i) and quality_2(i) and quality_3(i):
                print("YES")
            else:
                print("NO")
        break

    """用法：
    try:
        执行try中的指令，除非出现【问题】
    except 【问题】：
        出现【问题】，执行except后的指令。"""
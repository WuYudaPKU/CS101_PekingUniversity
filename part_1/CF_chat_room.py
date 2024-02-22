list_s = list(input())
list_result = []
list_hello=list("hello")
judge = 1
for index,item in enumerate(list_hello): #对每一个字母进行遍历
    try: #防止索引超出范围
        while item != list_s[index]:  #当第index个索引不是对应字母时，将字母删除
            try:
                list_s.remove(list_s[index])
            except IndexError: #删到出现错误，说明输入不合要求
                judge=0
                break
    except IndexError:#索引出现错误，说明输入不合要求
        judge=0

if len(list_s) <5:
    judge = 0
else:
    for i in range(5):
        list_result.append(list_s[i])

if "".join(list_result)=="hello":
    judge = 1

if judge == 0:
    print("NO")
elif judge==1:
    print("YES")
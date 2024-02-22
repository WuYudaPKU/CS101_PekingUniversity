# n是计划数
n=int(input())
raw=[]
for _ in range(n):
    start,end,value=map(str,input().split())
    if start[0]=="1":
        start=int(start.replace("1.",""))-6
    else:
        start=25+int(start.replace("2.",""))
    if end[0]=="1":
        end=int(end.replace("1.",""))-6
    else:
        end=25+int(end.replace("2.",""))
    value=int(value)
    if end<=45:
        raw.append(((start,end),value))
raw.sort(key=lambda x:x[0][1])
# print(raw,"\n")
dp=[[0 for _ in range(46)] for _ in range(len(raw))]
for row in range(len(raw)):
    if row==0:
        end=raw[0][0][1]
        for j in range(1,46):
            if j>=end:
                dp[row][j]=raw[0][1]
    else:
        start,end=raw[row][0]
        value=raw[row][1]
        for j in range(1,46):
            if j<end:
                dp[row][j]=dp[row-1][j]
            else:
                dp[row][j]=max(dp[row-1][j],value+dp[row-1][start-1])
    # for i in dp:
    #     print(i)
    # print("\n")
print(dp[-1][-1])
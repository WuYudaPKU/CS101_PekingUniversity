list_1 = list(map(int,input().split()))
n=list_1[0]
k=list_1[1]
list_up=[]
list_scores = list(map(int,input().split()))#n个成绩
for score in list_scores:
    if score >0 and score>= list_scores[k-1]:
        list_up.append(score)
print(len(list_up))
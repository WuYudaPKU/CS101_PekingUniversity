def TJ(arr1,arr2):
    a=len(arr1)
    b=a
    arr1.sort(reverse=True)
    arr2.sort(reverse=True)
    lst=[]
    for i in range(a):
        for j in range(i,a):
            if arr2[j]<=arr1[i]:
                temp=(i,j)
                lst.append(temp)
                break
    visited=set()
    success=0
    for tup in lst:
        for j in range(tup[1],b):
            if j not in visited:
                if arr2[j]==arr1[tup[0]]==arr2[min(j+1,b-1)]:
                    a-=1
                    visited.add(j)
                    break
                if arr2[j]==arr1[tup[0]]:
                    continue
                if arr2[j]>arr1[tup[0]]:
                    success+=1
                    visited.add(j)
                    break
    return 200*success-200*(a-success)

res=[]
while True:
    n=int(input())
    if n==0:
        break
    lst_1=list(map(int,input().split()))
    lst_2=list(map(int,input().split()))
    res.append(TJ(lst_1,lst_2))
for _ in res:
    print(_)
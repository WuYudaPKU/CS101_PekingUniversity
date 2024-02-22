"""
for an int with n spaces,like _ _ _ _ ,for all strs given,
 if a str S is put in the first place and any other strs put closely after
 it is bigger than the reverse, we say S is qualified for the first place.
 Then the second place, others are all the same.

the thought exactly corresponds with QuickSort."""
def QuickSort_small(lst):
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]>lst[j]+lst[i]:
                lst[i],lst[j]=lst[j],lst[i]
    return lst
def QuickSort_big(lst):
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]<lst[j]+lst[i]:
                lst[i],lst[j]=lst[j],lst[i]
    return lst
# lst_1=["232","233","23","231"]
# print(QuickSort(lst_1))
n=input()
lst_1=list(map(str,input().split()))
print("".join(QuickSort_big(lst_1)),"".join(QuickSort_small(lst_1)))
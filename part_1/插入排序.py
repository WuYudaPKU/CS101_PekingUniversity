def InsertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key< arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        print(arr)
lst=[3,2,4,1,5,3,6,7,34,42,5,235,12]
InsertionSort(lst)


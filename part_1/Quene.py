"""在开始之前先进行证明：
首先为了让前n个数的和尽可能小，我们先把队列升序排列；
接下来，我们在队列的左侧进行删除元素，并且加到前n个元素的和中，与剩下的队列的首个元素a(m)比较：
如果sum<a(m)，则把a(m)加入sum中
重点：如果sum>a(m)，我们考虑该把a(m)放在哪：
如果把这个元素放在更往前的位置，则一定至少有一个更小元素a(x<m)会替代这个元素的位置，使得不满意的顾客数至少是不变的(很可能是增加的)，
这对我们的目标没有任何帮助，所以只能把a(m)放在后面(>m)。
一旦把这个元素排在后面，这个顾客就更不能满意，所以他的位置对我们来说是无所谓的（牺牲这个顾客），
而如果把他放在当前队列的最后，可以让队首元素a(m+1)>=a(m)，其可能满意的概率也就更大，这符合我们的目标。"""

from collections import deque
n=int(input())
queue=deque(map(int,input().split()))
queue=deque(sorted(queue))
flag=0
dis=0
abs_flag=0
a=sum(queue)
while abs_flag<a:
    try:
        temp=queue.popleft()
        flag+=temp
        abs_flag+=temp
        if flag>queue[0]:
            dis+=1
            queue[0]=0
    except:
        break
print(n-dis)
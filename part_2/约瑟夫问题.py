#尝试自己使用链表
#1.定义单链表的节点（注意不是链表本身，而是其中的元素）
class Lnode:
    def __init__(self,data):#自身序号
        self.data=data
        self.next=None
#2.建立单链表
#区分首节点和头节点
#下面定义一个链表主体
class LinkList:
    def __init__(self):
        self.length=0
        self.next=None
    #a.判断是否为空表
    def is_empty(self):
        if self.next==None:
            return True
        else:
            return False
    #b.头插法建立单链表  插入后倒序
    def head_add(self,lnode):
        lnode.next = self.next
        self.next=lnode
        self.length+=1
    #c.尾插法建立单链表
    def tail_add(self,lnode):
        current_node=self
        if self.is_empty():
            self.next=lnode
        else:
            while current_node.next!=None:
                current_node=current_node.next
            current_node.next=lnode
            self.length+=1

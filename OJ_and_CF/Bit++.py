x=0
state_num = int(input())
list_states=[]
for i in range(state_num):
    list_states.append(list(input())) #列表里面嵌入列表[[+,+,X],[],[]]
for list in list_states:
    if "+" in list:
        x+=1
    elif "-" in list:
        x-=1
print(x)
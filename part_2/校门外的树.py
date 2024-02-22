L,M=map(int,input().split())
list_domains=[]
set_domains=set()
for i in range(M):
    list_domains.append(list(map(int,input().split())))#将区域作为列表嵌入在列表中
def f(domain): #domain是形如【a,b】的列表
    a=range(domain[0],domain[1]+1) #a是范围内所有自然数的集合
    return set(a)
#domain是列表
for domain in list_domains:
    set_domains.update(f(domain))#集合去重
result=L-len(set_domains)
print(result+1)
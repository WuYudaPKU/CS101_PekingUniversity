grades=list(i for i in range(100,59,-1))
def calculate(x):
    return 4-3*(100-x)**2/1600
print("成绩","绩点")
for i in grades:
    print(i,"{:.4f}".format(calculate(i)))
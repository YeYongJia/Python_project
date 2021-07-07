# 编写约瑟夫环，n为人数，q为每次计数,函数Joseph使用递归方法（方法一）
def Joseph_recursion(num,q):
    if num==1:
        return 0
    else:
        return (Joseph_recursion(num-1,q)+q) % num

#n1,q1 = eval(input('请输入人数n和计数单位q：'))# eval ：将 str 型转化为 int 型
#survived_num1 = Joseph_recursion(n1,q1)
#print('利用递归方法得到：number '+str(survived_num1 )+' survived') #编号 为从0到n-1

#约瑟夫环方法二：利用公式正序编写
def Joseph_formula(num,q):
    result = 0
    for i in range(2,num+1):
        result = (result+q)%i
    return result
#n2,q2 = eval(input('请输入人数n和计数单位q：'))# eval ：将 str 型转化为 int 型
#survived_num2 = Joseph_recursion(n2,q2)
#print('利用计算得到：number '+str(survied_num2 )+' survived') #编号

def Joseph_normal(num,q):
    queue = list(range(num))
#    print(queue)
    count = 0
    j = 0
    while len(queue) > 1:
        if j>len(queue)-1:
            j = 0
        if count == q-1:
            del queue[j]
            count = -1            
            j -= 1      
        j +=1
        count +=1
    return queue
n,q = eval(input('请输入人数n和计数单位q：'))# eval ：将 str 型转化为 int 型
survived_num = Joseph_normal(n,q)
print('利用计算得到：number '+str(survived_num)+' survived') #编号


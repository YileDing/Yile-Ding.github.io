#for循环解法
def _for_sum(n):
    total=0
    for i in n:
        total+=i
    return total

#while循环解法
def _while_sum(n):
    total=0
    i=0
    while i<len(n):
        total+=n[i]
        i+=1
    return total

#递归解法
def _recursion_sum(n):
    if n==[]:
        return 0
    else:
        return n[0]+_recursion_sum(n[1:])

#内置函数解法
#sum(n)

#列表推导式求和解法
def _list_sum(n):
    return sum([i for i in n])

#生成器表达式求和解法
def _generator_sum(n):
    return sum((i for i in n))

#并行求和(+嵌套)解法
def _divide_sum(n):
    if len(n)<=1:
        return n[0]
    else:
        _left_sum=_recursion_sum(n[0:len(n)//2])
        _right_sum=_recursion_sum(n[len(n)//2:])
        return _left_sum+_right_sum

#特殊解法之等差数列求和
def _special1_sum(first,last,n):
    if (last-first)//n%1!=0:
        return "请输入正确的数据！"
    else:
        return (first+last)*((last-first)//n+1)/2

#特殊解法之等比数列求和
def _special2_sum(first,last,n):
    if n==0:
        return "请输入正确的公比！"
    if n==1:
        x=int(input("请输入个数："))
        return first*x
    else:
        return (first-last*n)/(1-n)




        


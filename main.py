# YOUR CODE HERE
def summation(n):
    lst1=[]
    lst2=[]
    for i in range(n):
        num=int(input())
        lst1.append(num)
    for j in range(n):
        num=int(input())
        lst2.append(num)
    updated_list=[]
    for k in range(len(lst1)):
        result=lst1[k]+lst2[k]
        updated_list.append(result)
    return updated_list

def find_min_max(lst):
    max_num=lst[0]
    min_num=lst[0]
    for x in lst:
        if x>max_num:
            max_num=x
        elif x<min_num:
            min_num=x
    return min_num,max_num

n=int(input())
s=summation(n)
print(s)
print(find_min_max(s))

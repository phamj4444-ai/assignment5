l=[9,7,10,5]
def bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
        
bubble_sort(l)
print(l)

b = 1

def plus_1(a):
    a = a + 1
    return a

b = plus_1(b)
print(b)
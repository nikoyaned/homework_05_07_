
# factorial_with_caching

def factorial_with_caching (x,dict):
    if x == dict.keys():
        return dict.value ()
    if x <= 1:
        return 1
    y = x
    k = (x * factorial_with_caching (x-1, dict))
    dict[y] = k
    return (k)
    
    
d = {}
x  = int (input ())
y = x

factorial_with_caching(x, d)
print (d)
   





# fibonachi 
def fib (n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2) 
print (fib (3))








# def sum_of_elements(x): 

x = []
y = str (input ())
for i in y :
    x.append (int (i))

def sum_of_elements(x):
    k =0 
    for i in x :
        k+=i
    return k

print (sum_of_elements(x))









# binary_search

def binary_search (x,ls):
    start = 0
    end  = len(ls) - 1
    target  = int((start+end)/2)
    
    while ls [target] != x:
        target = int((start+end)/2)
        if ls[target] < x:
            start = target
        else :
            end = target 
    print (target)


binary_search (x = int( input ()),ls = [i for i in range (100)])











# Selection Sort

ls = [4,5,3,2,7,8,9,0,1,2,3,6]
for i in range (len(ls)) :
    min = i
    for j in range (i+1,len(ls)) :
            if ls[min] > ls[j]:
                 min = j
    temp = ls [i]
    ls[i] = ls[min]
    ls[min] = temp
print (ls)




# Bubble Sort

ls = [1,2,3,4,5,7,1,4,77,44,345,0,98,777,7,77]
print (ls)
for j in range (len(ls)-1) :
    for i in range (0,len(ls)-j-1):
        if ls [i] >ls[i+1]:
            ls[i],ls[i+1] = ls[i+1],ls[i]
print (ls)



# Insertion Sort

ls1 = [4,3,2,6,7,8,9,0,1,2,3]
for i in range (1,len(ls1)) :
    temp = ls1[i]
    j =i -1
    while j >= 0 and ls1[j] > temp :
        ls1[j+1] = ls1[j]
        j-=1
    ls1[j+1]= temp
print (ls1)
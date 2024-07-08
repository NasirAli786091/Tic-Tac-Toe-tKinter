import math
import os
import random
import platform

def operation(sign, n1, n2):
    if sign == '/':
        if n1 == 0:
            return n1/n2
        elif(n2 == 0):
            return n2/n1
        else:
            return n1/n2    
    if sign == '+':
        return n1 + n2
    if sign == '-':
        return n1 - n2
    if sign == '*':
        return n1 * n2
    
def operands():
        o = input("enter + - * /  = : ")
        return o

def calculator():
    n1 = int(input("Enter 1st number: "))
    # n2 = int(input("Enter 2nd number: "))
    res = 'NA'
    while(1):
        o = operands() #operands
        if o == '=':
            print(res)
            break
        n2 = int(input("Enter 2nd number: "))
        if o == '+':
            if(res == 'NA'):
                res = operation(o, n1, n2)
            else:
                # n3 = int(input("Enter a number: "))
                res = operation(o, res, n2)
        if o == '-':
            if res == 'NA':
                res = operation(o, n1, n2)
            else:
                res = operation(o, res, n2)
        if o == '*':
            if res == 'NA':
                res = operation(o, n1, n2)
            else:
                # n3 = int(input("Enter a number: "))
                res = operation(o, res, n2)
        if o == '/':
            if res == 'NA':
                res = int(operation(o, n1, n2))
            else:
                res = int(operation(o, res, n2))
        print(res)
# calculator()


def compundInt():
    p = int(input("Enter principal amount: ")) #principal
    r = int(input("Enter rate of interest: ")) #rate of interest
    n = int(input("Enter number of times compounded per year: ")) #rate of interest
    t = int(input("Enter time in year: ")) #time in year
    a = pow(p*(1 + (r/n), (n*t)))
    print(a)
# compundInt()


def primeNum():
    n = int(input("enter a number: "))
    count = 0
    if n==1:
        print(f"{n} is not a prime not composite")
    for i in range(1, n+1):
        if(n%i == 0):
            count+=1
    if(count<=2):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime")
# primeNum()
        


# def factorial():
#     n = int(input("enter a number: "))
#     res = 1
#     while n:
#         if n == 0:
#             res *= 1
#             break
#         else:
#             res*=n
#             n-=1
#     print(f"{res:,}")
# factorial()

def recurFactorial(n):
    if n == 0 or n == 1: 
        return 1
    return n * recurFactorial(n-1)

def facto():
    l1 = []
    while 1:
        n = int(input("enter a number: "))
        l1.append(str(recurFactorial(n)))
        a = input("want to continue Y or N: ")
        if a.lower() == 'n':
            print(", ".join(l1))
            break

def prob():
    keys =  ['first_name', 'age' , 'job', 'company']
    values =  ['Jim', 23, 'developer', 'XYZ']
    # myDict = dict(zip(keys, values))
    # print(myDict)
    i = 0
    myDict = {}
    while i < len(keys):
        myDict[keys[i]] = values[i]
        i+=1
    print(myDict)

def partition(arr, l, h):
    p = arr[l]
    i = l
    j = h
    while i < j:
        while i < h and arr[i] <= p:
            i+=1
        while j > l and arr[j] > p:
            j-=1
        if i < j:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
    t = arr[l]
    arr[l] = arr[j]
    arr[j] = t
    return j

def quickSort(arr, l, h):
    if l < h:
        j = partition(arr, l, h)
        quickSort(arr, l, j)
        quickSort(arr, j+1, h)
    return arr

def queston1(): #sort ascending to decending by value
    myDict = {
        'apple': 10,
        'banana': 5,
        'cherry': 12,
        'date': 7
    }
    myDictVal = []
    for i in myDict.values():
        myDictVal.append(i)
    
    return quickSort(myDictVal, 0, len(myDictVal)-1)

def question2():
    thisDict = {
        0 : 10,
        1 : 20
    }
    # thisDict[2] = 30 #indexing method
    thisDict.update({2 : 30}) #built in method
    print(thisDict)

def question3():
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    # for i in dic2.items():
    #     dic1[i[0]] = i[1]
    # for i in dic3.items():
    #     dic1[i[0]] = i[1]
    dic1.update(dic2)
    dic1.update(dic3)
    print(dic1)

def question4():
    dic={
        1:10,
        2:20,
        3:30,
        4:40,
        5:50,
        6:60
    }
    userK = int(input("Enter a number to check if available: "))
    if userK not in dic.keys():
        print("not available")
    else:
        print(f"value for key {userK} = ",dic[userK])


def question5():
    n = int(input("enter a number: "))
    myDic = {}
    for i in range(1, n+1):
        myDic[i] = i*i
    print(myDic)

def question6():
    dic = {}
    for i in range(1, 16):
        dic[i] = i*i
    print(dic)

def question8():
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
    # res = {}
    for i in d2.keys():
        if i in d1:
            d1[i] += d2[i]
        else:
            d1[i] = d2[i]
    print(d1)

def question9():
    l1 =  [{"V":"S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
    l2 = []
    for i in l1:
        val = list(i.values())[0]
        if val not  in l2:
            l2.append(val)
    print(l2)

def question10():
    tup = (3,4,1,5,7,0,2,10)
    max=tup[0]
    min=tup[0]
    for i in tup:
        if i > max:
            max = i
        if i < min:
            min = i
    print("minimum = ",min)
    print("maximum = ",max)

def question11():
    tup = ("hi", "my", "name", "is", "Nasir")
    res = ""
    for i in tup:
        res += i + " "
    print(res)


def fileHandling():
    fname = "name.txt"
    file = open(fname,'r')
    content = file.read()
    print(content)


def createOTP():
    n = ""
    while len(n) != 6:
        n += str(random.randint(0, 9))
    print(n)

def generatePass():
    print(random.random(ascii))


def bodmasProblems():
    i=0
    x = "1+2-3+6*50/50"
    numbers = []
    operations = []
    while i < len(x):
        if x[i] in ['+', '-', '/', '*']:
            operations.append(x[i])
            i+=1
        else:
            t = ''
            while i < len(x) and x[i] not in ['+', '-', '/', '*']:
                t += x[i]
                i+=1
            numbers.append(int(t))
    # print(numbers)
    # print(operations)
    print(eval(x))

def part(arr, l, h):
    p = arr[l]
    i = l
    j = h
    while i < j:
        while i < h and arr[i] < p:
            i+=1
        while j > l and arr[j] > p:
            j-=1
        if i < j:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
    t = arr[l]
    arr[l] = arr[j]
    arr[j] = t
    return j

def qSort(arr, l, h):
    if l<h:
        j = part(arr, l, j)
        qSort(arr, l, j)
        qSort(arr, j+1, h)

def kthSmallestEle():
    arr = [7, 10, 4, 3, 20, 15]
    kth = int(input("enter a number to find the kth smallest: "))
    quickSort(arr, 0, len(arr)-1)
    print(arr)
    for i in range(len(arr)):
        if i == kth-1:
            print(arr[i])
            break


def checkLast(pageR, curI, )

def LRUimplementation():
    s = "7012030423032"
    """
    7 7 7 7 7 3
      0 0 0 0 0
        1 1 1 1
          2 2 2

    """
    f = 0
    h = 0
    slot = 4
    pageRefe = [] #list of list
    pageT = [s[i] for i in range(slot)]
    # print(pageT)
    for i in range(slot, len(s)):
        if s[i] in pageT:
            h+=1
            continue
        else:
            pageRefe.append(pageT)



def palindromeList():
    # l1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    l1 = ["Nasir", "Rupam", "Nasir"]
    l2 = l1[::-1]
    if l1 == l2:
        print("Palindrome")
    else:
        print("not palindrome")

def main():
    # bodmasProblems()
    # kthSmallestEle()
    # palindromeList()
    LRUimplementation()

main()
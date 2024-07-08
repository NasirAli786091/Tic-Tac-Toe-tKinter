#functions in Python
# 1-> without parameter
def addNum():
    a = 10
    b = 20
    print("a+b = ", a+b)
# addNum()

# 2-> with parameter
def addNum(a, b):
    print("a + b =",a+b)
# addNum(10, 20)

# 2-> default parameter
def addNum(a, b=20):
    print("a + b =", a+b)
# addNum(20)
    


# HCF
def findHCF():
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    # if num1 >= num2:
    #     max = num1
    #     min = num2
    # else:
    #     min = num2
    #     max = num1
    max = num1 if num1 > num2 else num2
    min = num1 if num1 < num2 else num2
    while max > 0:
        if max % min == 0:
            print("the answer is =", min)
            break
        else:
            rem = max % min
            max = min
            min = rem
# findHCF()


# LCM
def GCD(n1, n2):
    #n1 > n2
    counter = n2
    while(n1 % counter != 0 or n2 % counter != 0):
        counter -= 1
    return counter
def findLCM():
    n1 = int(input("enter a number : "))
    n2 = int(input("enter a number : "))
    max = n1 if n1 >= n2 else n2
    min = n1 if n1 < n2 else n2
    # gcd = GCD(max, min)
    # lcm = (n1 * n2)//gcd
    print("LCM = ",(n1 * n2)//GCD(max, min))
# findLCM()
    


def calFact(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

def series(n):
    res = 0
    # switch = 1
    for i in range(1, n+1):
        # if switch == 1:
        if i % 2 == 1:
            res += 1/calFact(i)
            # switch = 0
        else:
            res -= 1/calFact(i)
            # switch = 1
    print(res)
# series(3)


def findSeries(n):
    for num in range(1, n+1):
        if(num % 2 == 1):
            print(num*num+1, end=" ")
        else:
            print(num*num-1, end=" ")
# findSeries(6)


def pattern1(n):
    for i in range(1, n+1):
        print("*"*i)
# pattern1(5)


# def checkPrime(n):
    # ..

def defineList():
    res = 0
    l2 = [2, 3, 5, 4, 7, 11, 8]
    for i in range(len(l2)):
        res += l2[i]
    print(res/i+1)
# defineList()

l2 = [1, 5, 6, 7, 7, 8, 1, 1, 1, 2, 2]
curE = sorted(l2)[0]
count=0
for i in range(0, len(l2.sort())):
    if(curE == l2[i]):
        count+=1
    else:
        print("curE = ", curE, "count = ", count)
        curE = l2[i+1]
        count=0
print(l2)
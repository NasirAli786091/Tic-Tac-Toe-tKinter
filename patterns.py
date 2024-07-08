# ****
# ****
# ****

def pattern1():

    for row in range(1, 4):
        for col in range(1, 5):
            print("*", end="")
        print()

# pattern1()




def pattern2(n):
    space = n-1
    stars = 1
    for i in range(0, n):
        #first print spaces
        for j in range(0, space):
            print(" ", end= "")
        
        #then print stars
        for k in range(0, stars):
            print("*", end="")
        
        print()
        space -= 1
        stars += 2
# pattern2(4)


def pattern3(n):
    space = n-1
    star = 1
    for row in range(n):
        #space
        for j in range(space):
            print(" ", end="")
        #stars
        for k in range(star):
            print("*", end="")
        print()
        space-=1
        star+=2
    space+=2
    star-=4
    for row in range(n-1):
        #space
        for j in range(space):
            print(" ", end="")
        #stars
        for k in range(star):
            print("*", end="")
        print()
        space+=1
        star-=2
# pattern3(4)


def pattern4(n):
    space = n-1
    star = 1
    for row in range(n):

        #space
        for j in range(space):
            print(" ", end="")
        
        #star
        for k in range(star):
            if(row == n-1):
                print("*", end="")
            elif(k == 0 or k == star-1):
                print("*", end="")
            else:
                print(" ",end="")

        print()
        space-=1
        star+=2
# pattern4(4)






def pattern5():
    for i in range(5):
        print("_", end="")
    print("|")
    for i in range(5):
        if i == 4:
            print("|")
pattern5()
# def calculateElectricBill(bill):
#     """
#         bill 300 -> 5rs/u
#              301 - 500 -> 7rs/u
#              501 - 999 -> 9rs/u
#     """
#     total = 0

#     if(bill <= 300):
#         total = bill * 5
#     elif(bill <= 500):
#         total = 300 * 5 + (bill - 300) * 7
#     else:
#         total = (300 * 5) + ((bill - 300) * 7) + ((bill - 500) * 9)
#     return total


# def main():
#     bill = int(input("enter bill amount: "))
#     print("total = ", calculateElectricBill(bill))
#     return 0

# main()

def printArr(arr):
    for i in arr:
        print(i, end=', ')
    print()

def merge(nums1, m, nums2, n):
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if (nums1[i] == 0):
            nums1[i] = nums2[j]
            i+=1
            j+=1
        elif (nums1[i] <= nums2[j]):
            i+=1
        else:
            t = nums1[i]
            nums1[i] = nums2[j]
            nums2[j] = t
            i+=1

nums1 = [4, 5, 6, 0, 0, 0]
nums2 = [1, 2, 3]
n = 3
m = 3
merge(nums1, m, nums2, n)
for i in nums1:
    print(i, end=', ')
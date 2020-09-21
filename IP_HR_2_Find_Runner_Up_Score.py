'''
Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
'''

#1 Using Set
n = 5
arr = [2 ,3 ,6 ,6 ,5]

arr_set = set(arr)
# print(arr_set)
arr_l = list(arr_set)
print(arr_l[-2])

#2 Sort

n = 5
arr = [2 ,3 ,6 ,6 ,5]

arr.sort()
print(arr)

max=arr[-1]
print(max)

n = len(arr)

n=-1
while arr[n]==max:
    print(arr[n])
    n-=1
print(arr[n])
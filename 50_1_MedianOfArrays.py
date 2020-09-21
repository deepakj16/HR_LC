arr1= [1,3,5]
arr2 = [2,4,6]

def median(arr1, arr2):
    return ( sum(arr1) + sum(arr2) ) / (len(arr1)+len(arr2))


print(median(arr1, arr2))
dict={}

def finddups(lis):
    for i in lis:
        if i not in dict:
            dict[i]=1
        else:
            dict[i] += 1
    print([ i for i in dict if dict[i] > 1])

print(finddups([3,3,3,2,2]))


arr=[3,3,3,2,2]
result_set = set()
#print(type(result_set))
#print(abs(arr[1]))


def find_duplicates(arr):
    """
    Return a list of duplicates in the array. To avoid using extra space,
    we flag which elements we've seen before by negating the value at
    indexed at that value in the array.
    """

    # Use a set for results to avoid duplicates.
    result_set = set()
    for i in range(len(arr)):
        # Translate the value into an index (1 <= x <= len(arr))

        idx = abs(arr[i]) - 1
        print(i, arr[i], abs(arr[i]), idx ,arr[idx]  )
        # If the value at that index is negative, then we've already seen
        # that value so it's a duplicate. Otherwise, negate the value at
        # that index we know we've seen it.
        if arr[idx] < 0:
            result_set.add(abs(arr[i]))
        else:
            arr[idx] = -arr[idx]
        print(result_set,arr)
    # Return the list to it's original state.
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

    return list(result_set)

print(find_duplicates(arr))
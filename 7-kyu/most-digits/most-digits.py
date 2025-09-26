def find_longest(arr):
    long = arr[0]
    for i in arr[1:]:
        if len(str(i)) > len(str(long)):
            long = i
        
    return long
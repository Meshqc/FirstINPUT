def reverse_by_center(s):
    mid = len(s) //2
    if len(s) % 2==0:
        final = s[mid:] + s[:mid]
    else:
        final = s[mid+1:] + s[mid] + s[:mid]
    return(final)
        
        
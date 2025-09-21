def disemvowel(s):
    vow = "aeiouAEIOU"
    for a in vow:
        s = s.replace(a,"")
    return s
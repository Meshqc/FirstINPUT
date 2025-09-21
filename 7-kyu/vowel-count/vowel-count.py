def get_count(sentence):
    count = 0
    vow = "aieou"
    for i in sentence:
        if i in vow:
            count += 1
    return count
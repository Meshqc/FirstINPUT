def get_villain_name(b): 
    first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    # your code here
    space = " "
    fname = ""
    if b.month == 1:
        fname = first[0]
    if b.month == 2:
        fname = first[1]
    if b.month == 3:
        fname = first[2]
    if b.month == 4:
        fname = first[3]
    if b.month == 5:
        fname = first[4]
    if b.month == 6:
        fname = first[5]
    if b.month == 7:
        fname = first[6]
    if b.month == 8:
        fname = first[7]
    if b.month == 9:
        fname = first[8]
    if b.month == 10:
        fname = first[9]
    if b.month == 11:
        fname = first[10]
    if b.month == 12:
        fname = first[11]
    lname = ""
    if b.day %10 == 0:
        lname = last[0]
    if b.day %10 == 1:
        lname = last[1]
    if b.day %10 == 2:
        lname = last[2]
    if b.day %10 == 3:
        lname = last[3]
    if b.day %10 == 4:
        lname = last[4]
    if b.day %10 == 5:
        lname = last[5]
    if b.day %10 == 6:
        lname = last[6]
    if b.day %10 == 7:
        lname = last[7]
    if b.day %10 == 8:
        lname = last[8]
    if b.day %10 == 9:
        lname = last[9]
    return fname + space + lname
​
​

# User's first input
def first_list():
    l1 = []
    while(True):
        input_1 = str(input("Please type in a hobby, interest, or course you've taken. "))
        l1.append(input_1)
        if len(l1) >= 5:
            break
    return l1

#User's friend input
def second_list():
    l2 = []
    while(True):
        input_2 = str(input("Please type in your friend's hobby, interest, or course he/she has taken. "))
        l2.append(input_2)
        if len(l2) >= 5:
            break
    return l2

# Jaccard Similarity Algorithm
def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

# Main
def main():
    print("We're going to determine how much you and your friend are a like")

    x = first_list()
    print(x)

    y  = second_list()
    print(y)

    if jaccard_similarity(x,y) < 0.20:
        print("You guys aren't very much a like")
    elif jaccard_similarity(x,y) > 0.20 and jaccard_similarity(x,y) < 0.50:
        print("You guys are somewhat a like!")
    else:
        print("You guys are very much a like!")

# Output
main()





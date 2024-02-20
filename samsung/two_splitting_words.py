def split_word(list1):
    word, seq=list1
    word_list=seq.split(",")
    print(word_list)
    for i in word_list:
        print(i, end="")
        if  word.startswith(i) in word_list:
            return word[len(i):]


print(split_word(["baseball", "a,ab,abc,b,ba,bas,base,bc,bce,ball,d,de,dec"]))

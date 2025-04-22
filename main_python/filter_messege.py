
def filter_messages(messeges):
    filtered_messeges = []
    count_words = []
    for i in range(0,len(messeges)):
        messege = messeges[i]
        non_words = []
        count = 0
        words = messege.split()
        for word in words:
            if word != "dang":
                non_words.append(word)
            else:
                count+=1
        main_messege = " ".join(non_words)
        filtered_messeges.append(main_messege)
        count_words.append(count)
    return filtered_messeges,count_words


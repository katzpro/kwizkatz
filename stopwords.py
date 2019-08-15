from nltk.corpus import stopwords


def exclude(update_list2, keyword, all_syn_anto):
    stop_words = set(stopwords.words('english'))
    string = ''
    for x in keyword:
        string = string + ' ' + x
    s = string.lstrip()
    for w in update_list2:
        if w not in stop_words:  # filtered_sentence.append(w)
            if (w in keyword or w in s) and w != '':
                print("\033[1;40m" + str(w) + "\033[1;m", end=' ')  # highlight - black
            elif w in all_syn_anto:
                print("\033[1;31m" + str(w) + "\033[1;m", end=' ')  # colourise - red
            else:
                print("\033[1;33m" + str(w) + "\033[1;m", end=' ')  # colourise - yellow
        else:
            print(w, end=' ')
    print('\n')
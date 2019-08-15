def keys(word_compare_list, keyword, diction):
    for m in range(3):
        n = 0
        indx = 0
        while n < len(word_compare_list):
            while indx < len(word_compare_list[n]):
                if keyword[m] == word_compare_list[n][indx]:
                    print('line #' + str(n+1) + ': key = ' + keyword[m])
                    diction[keyword[m]].append(str(n+1))
                else:
                    if indx < len(word_compare_list[n]) - 1:
                        new_compare = word_compare_list[n][indx] + ' ' + word_compare_list[n][indx + 1]
                        if keyword[m] == new_compare:
                            print('line #' + str(n + 1) + ': key = ' + keyword[m])
                            diction[keyword[m]].append(str(n + 1))
                indx += 1
            indx = 0
            n += 1
    return diction
from nltk.corpus import wordnet
from nltk.corpus import stopwords


def make_quiz(update_list2, keyword):
    stop_words = set(stopwords.words('english'))
    keyword2 = []
    ans = []
    string = ''
    count = 0
    for x in keyword:
        string = string + ' ' + x
    s = string.lstrip()
    for w in update_list2:
        if w in s and w not in stop_words and w != '':
            keyword2.append(w)
            print('... (' + str(count + 1) + ') ', end=' ')
            count += 1
        else:
            print(w, end=' ')
    print(keyword2)
    print('\nYour ans: ')
    for i in range(count):
        answer = input('Place (' + str(i+1) + ') ')
        ans.append(answer)
    m = 0
    while m < count:
        trial = 0
        if ans[m] != keyword2[m]:
            print('Incorrect answer at [' + str(m+1) +']')
            if keyword2[m] not in stop_words:
                print('Hint: definition of [' + str(m + 1) + '] ')
                print((wordnet.synsets(keyword2[m]))[0].definition())
            while ans[m] != keyword2[m] and trial < 3:
                print('\nIncorrect answer at [' + str(m + 1) + ']')
                trial += 1
                ans[m] = input('Replacement = ')
            if trial == 3 and ans[m] != keyword2[m]:
                print('\nYou run out of trials. Correct answer at [' + str(m + 1) + '] = ' + keyword2[m] + '\n')
                m += 1
        else:
            m += 1

    print('\nAll are now correct')






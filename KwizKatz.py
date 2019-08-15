class Text:
    def process_text(self):
        print('Your 3 keys: ')  # ask users to enter 3 keywords
        i = 0
        keyword = []
        while i < 3:
            key = input('Key #' + str(i + 1) + ' ')
            keyword.append(key)
            i += 1
        diction = {keyword[0]: [],
                   keyword[1]: [],
                   keyword[2]: []
                   }
        file_path = 'kwiz.txt'
        word_compare_list = []
        with open(file_path) as file_object:
            for line in file_object:
                line_copy = (line.lower()).replace('\n', '')  # make a copy of each line without \n at the end
                punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''  # define punctuations
                no_punct = ""
                for char in line_copy:
                    if char not in punctuations:
                        no_punct = no_punct + char  # no_puct += char
                word_compare_list.append(no_punct.split(' '))

        import keywords
        diction = keywords.keys(word_compare_list, keyword, diction)
        n = 0
        indx = 0
        update_list = []
        update_list2 = []
        while n < len(word_compare_list):
            while indx < len(word_compare_list[n]):
                update_list.append(word_compare_list[n][indx])
                update_list2.append(word_compare_list[n][indx])
                indx += 1
            indx = 0
            n += 1
        import suggestion
        all_syn_anto = suggestion.suggest(keyword, diction, update_list)
        print('Filtered text: ')
        import stopwords
        stopwords.exclude(update_list2, keyword, all_syn_anto)
        import quiz
        quiz.make_quiz(update_list2, keyword)


obj = Text
obj.process_text(Text)
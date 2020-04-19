import csv


def transform_array(filename, place_name):
    allcomment_in_place = []
    with open('./data/'+filename+'.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            matrixAr = []
            mystring = row[place_name]
            mystring = mystring.replace(' (', '(')
            mystring = mystring.replace("', '", ' - ')
            mystring = mystring.replace("'", '')
            b = mystring.replace("[[", "").replace("]]", "")
            for line in b.split('], ['):
                row_ = list(line.split(','))
                matrixAr.append(row_)
            allcomment_in_place.append(matrixAr)

    return allcomment_in_place


def find_word_distance(comments, noun_and_adj=True, noun_and_verb=True, noun_and_adv=True):
    words_distance = []
    for comment in comments:
        for sentence in comment:
            i = 0
            while i < len(sentence):

                if sentence[i].find("NOUN") != -1:
                    j = i+1
                    while j < len(sentence) :
                        if (sentence[j].find("ADJ") != -1 and noun_and_adj) \
                                or (sentence[j].find("VERB") != -1 and noun_and_verb) \
                                or (sentence[j].find("ADV") != -1 and noun_and_adv):

                            print(f"{sentence[i]} and {sentence[j]} with {j-(i+1)}")

                        j += 1
                i += 1


comments = transform_array("google", "patong")
find_word_distance(comments)

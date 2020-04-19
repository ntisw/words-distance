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
    dist_noun_and_verb = []
    dist_noun_and_adv = []
    dist_noun_and_adj = []
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
                            distance = j-(i+1)
                            if sentence[j].find("ADJ") != -1 and noun_and_adj : 
                                dist_noun_and_adj.append({"noun":sentence[i] 
                                ,"adj":sentence[j]
                                ,"distance":distance
                                })

                            if sentence[j].find("ADV") != -1 and noun_and_adv :
                                dist_noun_and_adv.append({"noun":sentence[i] 
                                ,"adv":sentence[j]
                                ,"distance":distance
                                })

                            if sentence[j].find("VERB") != -1 and noun_and_verb :
                                dist_noun_and_verb.append({"noun":sentence[i] 
                                ,"verb":sentence[j]
                                ,"distance":distance
                                })

                            #print(f"{sentence[i]} and {sentence[j]} with {distance}")

                        j += 1
                i += 1
        words_distance.append(dist_noun_and_adj)
        words_distance.append(dist_noun_and_adv)
        words_distance.append(dist_noun_and_verb)
    return words_distance

def write_file(words_distance) :
    max_len = 0
    if len(words_distance[0]>= max_len) :
        max_len = words_distance[0] 
    print(len(words_distance[0]))
    print(len(words_distance[1]))
    print(len(words_distance[2]))


comments = transform_array("google", "patong")
words_distance = find_word_distance(comments)
write_file(words_distance)

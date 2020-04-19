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

def write_file(words_distance,filename) :



    # field names  
    fields = ['noun', 'adj', 'distance', 'noun','adv','distance','noun','verb','distance']  
        
    # data rows of csv file  
    rows = transform_array_for_writefile(words_distance)     
        
    # writing to csv file  
    with open(filename, 'w',encoding='utf-8') as csvfile:  
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile)  
            
        # writing the fields  
        csvwriter.writerow(fields)  
            
        # writing the data rows  
        csvwriter.writerows(rows) 





def transform_array_for_writefile(words_distance) :
    lens = [len(words_distance[0]),len(words_distance[1]),len(words_distance[2])]
    max_len = max(lens)
    transform_array = []
    i = 0
    while i < max_len :
        row = []
        noun_adj = ""
        noun_adv = ""
        noun_verb = ""
        adv = " "
        adj = " "
        verb = " "
        distance_adj = " "
        distance_adv = " "
        distance_verb = " "
        if len(words_distance[0]) > i :
            noun_adj = words_distance[0][i]["noun"]
            adj = words_distance[0][i]["adj"]
            distance_adj =  words_distance[0][i]["distance"]

        if len(words_distance[1]) > i :
            noun_adv = words_distance[1][i]["noun"]
            adv = words_distance[1][i]["adv"]
            distance_adv = words_distance[1][i]["distance"]

        if len(words_distance[2]) > i  :
            noun_verb = words_distance[2][i]["noun"]
            verb = words_distance[2][i]["verb"]
            distance_verb = words_distance[2][i]["distance"]

        row.append(noun_adj)    
        row.append(adj)
        row.append(distance_adj)
        row.append(noun_adv)
        row.append(adv)
        row.append(distance_adv)
        row.append(noun_verb)
        row.append(verb)
        row.append(distance_verb)
        transform_array.append(row)
        i+=1

    print(f"MAX LEN = {max_len}")
    print(len(words_distance[0]))
    print(len(words_distance[1]))
    print(len(words_distance[2]))
    
    return transform_array

filename = "google_patong.csv"
comments = transform_array("google", "patong")
words_distance = find_word_distance(comments)
write_file(words_distance,filename)

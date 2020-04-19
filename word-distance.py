import csv
def transform_array(filename,place_name):
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

def find_word_distance(comments,noun_and_adj = True ,noun_and_verb = True , noun_and_adv =  True ) :
    words_distance = []
    for comment in comments :
        for sentence in comment :
            for word in sentence:
                print (word)



comments = transform_array("google","patong")
find_word_distance(comments)

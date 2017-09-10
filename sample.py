import random


# Sampling
indexVal = 0
reviewVal = []
reviewStringsVal = []
keyword = {}
data = ''
dataString = ''
index = 0
rand = random.randint(1, 11)
position = (rand - 1) * 9
position = 0
docCount = 0
with open('foods.txt', 'r') as infile:
    for (indexVal, myString) in enumerate(infile):
        myString = unicode(myString, errors='ignore')
        if indexVal >= position:
            # print indexVal, myString
            if myString and myString.strip():
                dataString = dataString + '\n' + myString
                array = myString.split(':')
                if array[0] == 'review/text' or array[0] == 'review/summary':
                    data = data + array[1]
            else:
                docCount += 1
                x = [x.lower().strip() for x in data.split()]
                a = set()
                for elem in x:
                    a.add(elem)
                    if elem not in keyword.keys():
                        temp = set()
                        temp.add(index )
                        keyword[elem] = temp
                    else:
                        keyword[elem].add(index)
                index += 1
                reviewVal.append(a)
                reviewStringsVal.append(dataString)

                data = ''
                dataString = ''
            if docCount == 100:
                break
        else:
            continue

keywordFile = open('keyword.txt', 'w+')
search_url = 'http://127.0.0.1:5000/api?search_token='
i = 0
while i < 100000:
    N = random.randint(1, 11)
    x = random.sample(keyword.keys(), N)
    line = ','.join(x)
    line = search_url + line
    keywordFile.write(line)
    keywordFile.write('\n')
    i = i + 1
keywordFile.close()
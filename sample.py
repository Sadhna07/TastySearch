import random


# Read a input file foods.txt
# read line by line in loop using enumeration which adds counter or index to iterator. [it works till the condition satisfies]
    # check if index is greater or equals to 0, if yes, then:
        # check if each line (string) is present in a file then
            # add the data (strings) to variable String (dataString)
            # check if string contains 'review/text' or 'review/summary', as these parameter are further used for calculating the scores.
                # store these parameter value to a variable String(data)---keywords set.
        # if no that is blank line(present after each review), then check the data string where all the keywords stored, and split it
            # now loop around the data string values and store in set to make it unique( remove duplicate keyword ).
            # Storing each keyword along with its index in the dictionary named keywords(key: keyword, value: index)
            # store unique keywords data to list variable reviewVal  as per the indexand the input review data to list reviewStringsVal.
        # checking the doccount to avoid delay the computation time while testing.


# writing to a file named keywords.txt keywords along with a url:'http://127.0.0.1:5000/api?search_token='
# reading the dictionary keywords containg index and key strings and writing to file along with url.


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
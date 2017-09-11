# TastySearch
Search Engine


Command to run on linux: (foods.txt should be in current directory)

export FLASK_APP=app.py
python -m flask run


Sampling and Indexing:
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


Searching:
# Taking the input from the url text box using request.args.get
# now passing that to search api

# In search API:::
# Splitting the input parameter by comma and space and checking length of token is not equals to zero
# check if token is present in keyword dictionary((key: keyword, value: index)) and set that value to keywordSearch list
# check if keywordSearch length is quals to zero or not:
	# zero, return empty string
	# not zero, then check if matched keyword in reviewVal String
		# calculate the score on match that is count / length for each index, that is for each review data.
		# then sort the matched result
		# now append the calculated score to the reviewStringsVal list, and return.
from __future__ import division
from flask import Flask, request, render_template, jsonify, flash, session
import random, os
import numpy as np
from sample import *

app = Flask(__name__)

# Searching:
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



def search(token):
	try:
		# print token
		token = [x.lower().strip() for x in token.split(',')]
		if len(token) != 0:
			index = 0
			searchResult = []
			documents = []
			length = len(token)
			keywordSearch = [keyword[elem] for elem in token if elem in keyword.keys()] 
			keywordSearch = set().union(*keywordSearch)
			# print keywordSearch, len(keywordSearch)

			if len(keywordSearch) == 0:
				return ['Empty Search']

			result = [0] * (max(keywordSearch) + 1)
			# print keywordSearch
			for x in keywordSearch:
				count = 0
				for y in token:
					if y in reviewVal[x]:
						count += 1
					else:
						pass
				result[x] = count / length
			final_result = list((np.argsort(result)[::-1])[:20])

			i = 0
			for x in final_result:
				if result[x] != 0:
					searchResult.append(str(reviewStringsVal[x]) + 'Score: ' + str(result[x]) )
					i = i + 1
				else:
					pass
				
			return searchResult
			pass
		else:
			return ['Empty Search']
	except Exception, e:
		return str(e)



@app.route('/', methods=['GET', 'POST'])
def index():
	try:
		if request.method == 'POST':
			searchKeyword = request.form['search']
			searchResult = search(searchKeyword)
			return render_template('result.html', data=searchKeyword, var=searchResult)
		else:
			return render_template('index.html')
	except Exception, e:
		flash(e)


@app.route('/result')
def result():
	return render_template('result.html')


@app.route('/api', methods=['GET'])
def api():
	try:
		searchKeyword = request.args.get('searchKeyword')
		searchResult = search(searchKeyword)
		searchEngine = {'searchKeyword': searchKeyword, 'searchResult': searchResult}
		return (jsonify({'searchEngine': searchEngine}), 200)
	except Exception, e:
		return (str(e) + 'ERROR' + str(searchResult), 400)
		flash(e)



if __name__ == '__main__':
	app.run(debug = True, secret_key = 'secret11232234535465676b')

			

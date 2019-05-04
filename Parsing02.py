import urllib.request
import re
import matplotlib.pyplot as plt
import numpy as np

author = input("Please input the name of author: ")
print("[ Author: " + author + " ]")##input the author
##test(Ian+Goodfellow)
number = 0
Namelist = [] #set timelist to record the total data in namelist
while number < 1000: #do for loop 1000 datas
	url = "https://arxiv.org/search/?searchtype=author&query=" + author + "&abstracts=show&size=200&order=-announced_date_first&start=" + str(number)
    #according the rule of the website, get the data from different pages
    content = urllib.request.urlopen(url) #to get date form url
        html_str = content.read().decode('utf-8') # to decode the url
	number += 200
	pattern = 'Authors:</span>[\s\S]*?</a>'
    #take the string of the rul from "Authors: to </a>"
	result = re.findall(pattern, html_str)
    #storage the data to string type, name result
	i = 0
	for r in result:
		name = r.split("Authors:</span>")[1].split("</a>")[0]
        #split the string what you want according the rule\
        #finally get the string contain with </a> tag
		name = re.sub('<[^>]*>', '', name)
        #remove the </a> tag from the string
		name = name.lstrip()
		Namelist.append(name)
        #set the author name in the namelist
		i += 1
	if number == 2000:
		break
class_number = []
class_name = list(set(Namelist)) #set the no-reapting data in the number list
class_name.sort() #sor the name in the list from a-z A-Z


for i in range(len(class_name)):
	class_number.append(Namelist.count(class_name[i]))
	print("[ co-author " + class_name[i] + "\t\t\t]:" + str(class_number[i]))
    ##print out the result
	##Ian+Goodfellow	

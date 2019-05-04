import urllib.request
import re
import matplotlib.pyplot as plt
import numpy as np

author = input("Please input the name of author: ")
print("[ Author: " + author + " ]")##input the author
##test(Ian+Goodfellow)
number = 0
Timelist = [0] #set timelist to record the total data
while number < 1000:  #do for loop 1000 datas
	url = "https://arxiv.org/search/?searchtype=author&query=" + author + "&abstracts=show&size=200&order=-announced_date_first&start=" + str(number)
        #according the rule of the website, get the data from different pages
    content = urllib.request.urlopen(url) #to get data of url
    html_str = content.read().decode('utf-8')  #to decode url
	number += 200
	pattern = '<span class="has-text-black-bis has-text-weight-semibold">originally announced</span>[\s\S]*?</p>'
    #take the string of the url from "<span to <\p>"
	result = re.findall(pattern, html_str)
    #storage the data to string type, name result
	i = 0
	for r in result:
		time = r.split("has-text-black-bis has-text-weight-semibold\">originally announced</span>")[1].split("</p>")[0].strip().split('\s')
        #split the string what you want according the rule
		time = re.findall(r"\d+\d*",str(time))
        #take the time of the string and change the type to int,finaly set the int() in the time
		Timelist += list(map(int, time))
        #set every time data to time list
		i += 1
	if number == 2000:
        print(Timelist)#finally get all the publish time in timelist
		break
Timelist.remove(0)
class_y = []  #set the pattern y of the list
class_x = list(set(Timelist)) #set the no-reapting timedata to the x list
class_x.sort()  #sort the x list
print (class_x)  #test the data I catch is right or not

for i in range(len(class_x)):
    class_y.append(Timelist.count(class_x[i])) #count the data of the timelist ,and storage in the y list

print (class_y)  #test the data I catch is right or not
plt.bar(class_x, class_y, label = 'class_a')  #draw the plot
plt.show()  #print the plot


	##Ian+Goodfellow	

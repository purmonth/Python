import urllib.request
import re
import matplotlib.pyplot as plt
import numpy as np

author = input("Please input the name of author: ")
print("[ Author: " + author + " ]")
number = 0
Namelist = []
while number < 1000:

	url = "https://arxiv.org/search/?searchtype=author&query=" + author + "&abstracts=show&size=200&order=-announced_date_first&start=" + str(number)
	##url = "https://arxiv.org/search/?query=" + author + "&searchtype=author"
	content = urllib.request.urlopen(url)
	html_str = content.read().decode('utf-8')
	##print(html_str)
	number += 200
	pattern = 'Authors:</span>[\s\S]*?</a>'
	##print(pattern)
	result = re.findall(pattern, html_str)
	###print(result)

	i = 0
	for r in result:
		name = r.split("Authors:</span>")[1].split("</a>")[0]
		name = re.sub('<[^>]*>', '', name)
		##name = [x.strip(' ') for x in name]
		name = name.lstrip()
		##print(name)
		##print(i)
		Namelist.append(name)
		
		i += 1
	
	if number == 200:
		##print(Namelist)
		break
class_number = []
class_name = list(set(Namelist))
class_name.sort()
##print("\n")
##print(class_name)

for i in range(len(class_name)):
	class_number.append(Namelist.count(class_name[i]))
	print("[ co-author " + class_name[i] + "\t\t\t]:" + str(class_number[i]))




'''
class_y = []
class_x = list(set(Timelist))
class_x.sort()
##print (class_x)

for i in range(len(class_x)):
    class_y.append(Timelist.count(class_x[i]))

##print (class_y)
plt.bar(class_x, class_y, label = 'class_a')
plt.show()

'''
	##Ian+Goodfellow	

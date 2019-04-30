import re
my_string = '<FNT name="Century Schoolbook" size="22">Title</FNT>'
print (re.sub('<[A-Za-z\/][^>]*>', '', my_string))
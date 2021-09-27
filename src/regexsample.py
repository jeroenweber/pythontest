import re
a = 'ap,ple , '

a = re.sub('[ ,]','',a)
print(a)
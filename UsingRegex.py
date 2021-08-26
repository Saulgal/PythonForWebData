#import libraries for regex
import re

#Open the file
x = open('teste.txt')

#create variable to store the sum
num_list = list()

for line in x:
    line = line.rstrip()
    thing = re.findall('[0-9]+', line)
    if len(thing) == 0: continue
    # print(thing)
    num = sum([float(i) for i in thing])
    # print(num)
    num_list.append(num)

print(sum(num_list))

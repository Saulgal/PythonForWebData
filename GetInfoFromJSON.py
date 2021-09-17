# import urllib library
from urllib.request import urlopen

# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "http://py4e-data.dr-chuck.net/comments_1327115.json"

# store the response of URL
response = urlopen(url)

# storing the JSON response 
# from url in data
info = json.loads(response.read())

# print(json.dumps(info, indent=2))

#create variable to store the sum
num_list = list()

for item in info['comments']:
    # print('Name', item['name'])
    # print('count', item['count'])
     #Store the value of content in num
    num = float(item['count'])
    num_list.append(num)
    
print(sum(num_list))

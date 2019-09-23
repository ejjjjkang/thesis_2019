
from io import open
import json
import os.path

"""
불용어 제거할 것 
1. 숫자
2. 한글자

"""

# save json file to text
PATH = './'


dataType = ['test', 'train', 'valid']


for i in range(len(dataType)):

    commentText = []
    with open(PATH + str(dataType[i])+'_progressive.json', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

        for json_string in json_data:
            commentText.append(json_string['commentText'])

        str1 = ''.join(commentText)
        f = open(str(dataType[i])+ '_progressive.txt', 'w')

        f.write(str1)
        str1 = ''
        f.close()


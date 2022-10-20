import numpy as np
from SegmentPage import segment_into_lines
from SegmentLine import segment_into_words
from RecognizeWord import recognize_words
import random
import os
import requests
import re


#Open image and segment into lines
fileName = random.choice(os.listdir("C:\\Users\\0014Q7744\\Documents\\Dissertation_Final\\Test_Images"))
print(fileName)
response = requests.get("http://localhost:8000/get-files/"+fileName)
line_img_array=segment_into_lines("C:\\Users\\0014Q7744\\Documents\\Dissertation_Final\\Test_Images\\"+fileName)


#Creating lists to store the line indexes,words list.
full_index_indicator=[]
all_words_list=[]
#Variable to count the total no of lines in page.
len_line_arr=0

#Segment the lines into words and store as arrays.
for idx,im in enumerate(line_img_array):
    line_indicator,word_array=segment_into_words(im,idx)
    for k in range(len(word_array)):
        full_index_indicator.append(line_indicator[k])
        all_words_list.append(word_array[k])
    len_line_arr+=1
    

all_words_list=np.array(all_words_list)


#Perform the recognition on list of list of words.
recognize_words(full_index_indicator,all_words_list,len_line_arr)

f = open("recognized_texts.txt","r")
lines = f.readlines()
print(lines)
for line in lines:
    if line.__contains__("bertrand" or "confounded"):
        print("contain")
        resp = requests.get("http://localhost:8000/get-logs/bertrand")
        logs = resp.text
        r = re.compile('[a-zA-Z0-9]+Exception')
        listOfException = r.findall(logs)
        finalList = []
        for ex in listOfException:
            if ex not in finalList:
                finalList.append(ex)

        print("Exception coming for this defect is : \n")
        print(finalList)


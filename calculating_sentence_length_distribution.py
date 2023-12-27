import re
import matplotlib.pyplot as plt
import os
import csv


def sort_and_print(count, step):
    histogram = {}
    keys = count.keys()
    max_length = max(keys)
    for i in range(1, max_length + 1, step): 
        this_key = "{}--{}".format(i, i+step-1)
        for key, value in count.items():
            if key >= i and key < i + step:
                histogram[this_key] =  histogram.get(this_key, 0) + value


    his_list = list(histogram.items())
    Excel = open("SL_year_distribution.csv", 'w', newline='')  #open a new csv file for sentence length distribution data
    writ = csv.writer(Excel)
    writ.writerow(['lenth level', 'frequency'])   
    
    # his_list.sort(key=lambda x:x[1], reverse=True) 
    for x in his_list:
        writ.writerow(x)  
    Excel.close()
    
    with open("SL_year.txt",'w',encoding='utf-8') as f:   #"SL_year.txt" is the prepared subtitle file
        for i in range(len(his_list)):
            f.write("{} {}\n".format(i+1, his_list[i][1]))
        
    f.close()


def calculate_avg_length(s, count):
    size = 0
    num = 0

    sentences = re.split(r' *[\.\？?!！.。][\'"\)\]]* *', s)

    print(sentences)
    for stuff in sentences:
        addsize = len(stuff.split())
        count[addsize] = count.get(addsize, 0) + 1
        size = size + addsize 
        num = num +1

    print("avg_length_num is "+str(size/num))


path = os.getcwd()
path += '/data'  #subtitle file(s) to be calculated stored in this folder
count = {}
os.chdir(path)
for f in os.listdir():
    if f.endswith("txt"):
        with open(f,'r',encoding='utf-8') as f:
            s = f.read()
            s = re.sub('/C', '', s)
            s = re.sub('\r|\n|', '', s)
        f.close()
       
        calculate_avg_length(s, count)
    
print(count)
step = 3  #set the length level interval
sort_and_print(count, step)




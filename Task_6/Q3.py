import random
import os

count = 0
maxCount = 0
words_list = []
word = "" 
file = open("C:/Users/VARSHA/Cognizance/Task_6/about.txt", "r")  
      
#Gets each line till end of file is reached  


text = file.read()
text = text.replace(",", "")
text = text.replace(".", "")
words = text.split(" ")
    
for i in range(0, len(words)):  
    count = 1
    for j in range(i+1, len(words)):  
        if(words[i] == words[j]):  
            count = count + 1
                    
    if(count > maxCount):  
        maxCount = count  
        word = words[i]

    if(len(words[i]) >= 6):  
        words_list.append(words[i])


print("6 letter most repeated words:", word)
print("\n6 letter words words",words_list)
file.close()
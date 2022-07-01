import csv
import re


file = open('C:/Users/VARSHA/Cognizance/Task_6/onelinefile.txt', 'r')
text = file.read()

#filtering float
floats = []
pattern = "\d+\.\d+"
floats=re.findall(pattern,text)


#filtering strings
strings = re.findall('[A-z]+',text)

#filtering int
ints = []
str_list = re.findall('\d+\.?\d*',text)
for i in str_list:
    try:
        ints.append(int(i))
    except:
        pass

csv_file = open('C:/Users/VARSHA/Cognizance/Task_6/Filename2.csv', 'w',  newline='')
writer = csv.writer(csv_file)

# to insert in a single column
count = 0
for i in range(len(ints)):
    row = [str(ints[i]) + "," + strings[count] + "," + floats[i] + "," + strings[count+1]]
    writer.writerow(row)
    count += 2
    
#to insert in a separate column
count = 0
for i in range(len(ints)):
    row = [ints[i] , strings[count] , floats[i] , strings[count+1]]
    writer.writerow(row)
    count += 2


file.close()
csv_file.close()

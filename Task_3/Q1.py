from typing import List

List = []

first_num = int(input("Enter the first value: "))
last_num = int(input("Enter the last value: "))

first=min(first_num,last_num)
last=max(first_num,last_num)
for i in range(first,last+1):
    List.append(i)
    print(i)
    for j in range(5):
        List.append(0)
print(List)
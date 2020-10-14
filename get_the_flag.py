#!/usr/bin/env python
import string 

result = string.ascii_lowercase;
numbers_of_title = [];
chart_of_title = [];
numbers_of_flag = [];
chart_of_flag = [];


elements_of_title = int(input("Enter the number of elements in title: "));

for i in range (0, elements_of_title):
    elements = int(input());
    numbers_of_title.append(elements);

for i in numbers_of_title:
    chart_of_title.append(result[i -1])

elements_of_flag = int(input("Enter the number of elements in flag: "));

for i in range (0, elements_of_flag):
    new_elements = int(input());
    numbers_of_flag.append(new_elements);

for i in numbers_of_flag:
    chart_of_flag.append(result[i -1])

print(*chart_of_title, sep=""); print("{");
print(*chart_of_flag, sep=""); print("}");

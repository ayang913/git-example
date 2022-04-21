#!/usr/bin/env python
# coding: utf-8

# In[95]:


a = 0
f = open('testfile_ex1.txt', 'r')
import io
buf = io.StringIO()
mylist2 = []
with open('testfile_ex1.txt') as f:
    mylist = f.read().splitlines()
    
for x in mylist:
    str = x.replace("\n", "")
    if (str != ""):
        mylist2.append(x.replace("\n", ""))
    
pos = 0
num = 0
j = -1
sw = True
door = 0
count = 0
for item in mylist2:
    if (pos >= len(mylist2)):
        break
    if (pos < len(mylist2)):
        num = int(mylist2[pos])
        pos = pos+1
        
    list = []
    for i in range(pos, pos+num):
        tmp = pos
        end = pos+num
        if ( i > pos ):
            str1 = mylist2[i-1]
            str2 = mylist2[i]
            if (str1[len(str1)-1] == str2[0]):
                ("")
            else:
                door = door+1                                                                                                                                         
                print('Secret Door ', door)  
                print('Can not be opened.\n')
                break
            
            if (i == pos+num-1):
                door = door + 1 
                print('Secret Door ', door)
                print('Can be opened.')
                for k in range(tmp, end):
                    print(mylist2[k], end = '')
                    if (k != end-1):
                        print('-', end = '')
                    else:
                        print('\n')
                break
    pos = pos+num


# In[ ]:





# In[ ]:





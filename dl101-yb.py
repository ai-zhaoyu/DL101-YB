# -- coding: utf-8 --
from sys import argv

script,filename=argv
data=open(filename,'r')
words_list=data.read().split(' ')
lens_words_list=len(words_list)

#删除列表中因连续空格造成的空字符，使用字符长度判断字符列表后就没用了
delete_item=[]
m=0
for i in range(0,lens_words_list):
    if words_list[i]=='':
    j=i-m
    delete_item.append(j)
    m+=1

for i in delete_item:
    del words_list[i]

lens_words_list=len(words_list)
ey_dict={}
m=0
#tcfh_list=['，','。','―','：','“','”','的','是']
for i in range(0,lens_words_list-1):
#    if (words_list[i] in tcfh_list) or (words_list[i+1] in tcfh_list):
    if len(words_list[i])<=3 or len(words_list[i+1])<=3:
        continue
    else:
        m+=1
        ey_words=words_list[i]+' '+words_list[i+1]
        if ey_words not in ey_dict:
            ey_dict[ey_words]=1
        else:
            ey_dict[ey_words]+=1

ey_dict_sort = sorted(ey_dict.items(),key = lambda ey_dict:ey_dict[1],reverse = True)

for i in range(0,10):
    print ey_dict_sort[i][0].decode('utf-8').encode('GBK'),ey_dict_sort[i][1],ey_dict_sort[i][1]*10000.0/m
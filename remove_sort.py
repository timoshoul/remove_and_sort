
def removeDuplicates(alist):
    a_list=[]
    for i in alist:
        if i not in a_list:
            a_list.append(i)
        
    return a_list
                
def sortList(alist):
    alist.sort();
    return alist;
        
    

a_list=[10, 12, 14, 14, 16, 28, 28, 30]
a_list=removeDuplicates(a_list)
print(a_list)
a_list=sortList(a_list)
print(a_list)

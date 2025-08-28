#25-08-2025
'''print(id(10))'''

#GENERAL COPY
#normal list
'''source1=[10,20,30,40,50]
print(source1)
print(id(source1))
destination1=source1
print(destination1)
print(id(destination1))
source1[2]=75 #changing value of sorce to check if it reflects in destination
print(source1)
print(destination1)
destination1[3]=88 #changing destination value to check if it reflects in source
print(source1)
print(destination1)'''

#Nested List
'''source2=[1,2,['abc',4],5]
destination2=source2
print(source2)
print(destination2)
print(id(source2))
print(id(destination2))
source2[2]=78
print(source2)
print(destination2)'''

'''source3=[1,2,['abc',4],5]
destination3=source3
print(source3)
print(destination3)
print(id(source3))
print(id(destination3))
source3[2][0]='def'
print(source3)
print(destination3)'''

#26-08-2025
#SHALLOW COPY

#linear list
'''l1=[1,2,3,4]
d=l1.copy()
l1[2]=20
print(l1)
print(id(l1))
print(d)
print(id(d))'''

#nested list
'''lst1=[1,'abc',['abc',3],4]
print(lst1)
print(id(lst1))
print()
lst2=lst1.copy()
lst1[2]=[7,8]
print(lst1)
print(id(lst1))
print(lst2)
print(id(lst2))
lst2[2]=3
print(lst1)
print(id(lst1))
print(lst2)
print(id(lst2))'''

'''l=[1,2,[3,4]]
d=l.copy()
d[2][0]=7
print(l)
print(id(l))
print(d)
print(id(d))

original_list = [[1, 2], [3, 4]]
shallow_copied_list = list(original_list) # Or original_list.copy()

# Modify a nested list in the shallow copy
shallow_copied_list[0][0] = 99

print(original_list)        # Output: [[99, 2], [3, 4]]
print(shallow_copied_list)  # Output: [[99, 2], [3, 4]]

original_list = [[1, 2], [3, 4]]
shallow_copied_list = list(original_list)

# Reassign a top-level element in the shallow copy
shallow_copied_list[0] = [5, 6]

print(original_list)        # Output: [[1, 2], [3, 4]]
print(shallow_copied_list)  # Output: [[5, 6], [3, 4]]'''




#DEEP COPY
import copy
l=[1,2,3,4]
d=copy.deepcopy(l)
l[2]=23
print(l)
print(id(l))
print(d)
print(id(d))
l1=[1,2,[3,4],5]
l2=copy.deepcopy(l1)
l1[2][0]=72#changes will reflect only in l1
print(l1)
print(id(l1))
print(l2)
print(id(l2))

l1[2]=72 #changes will reflect in only l1
print(l1)
print(id(l1))
print(l2)
print(id(l2))







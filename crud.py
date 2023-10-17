#create/add data to list:

#Append

#syntax:lst.append(item)

name=["Navya","Rajesh"]
name.append("Mahalya")
print(type(name))
print(name)

#insert

#syntax:variableName.insert(index,item)

name=["Navya","Rajesh","Mahalya"]
name.insert(2,"Pranathi")
print(name)


#Read-Access/getitems from the list:

#By using index
#index method
#list slicing

#syntax:lst[index]

city=["Hyderabad","Guntur","Vijayawada"]
print(city.index("Guntur"))

#Fix
#count

city=["Hyderabad","Guntur","Vijayawada"]
print(city.count("Guntur"))
print(city.count("Dachepalli"))

name=["Navya","Rajesh","Mahalya"]
if(name.count("Sagar")>0):
    print(name.index("Sagar"))


#update

#by using index

#syntax:variableName[index]=data

name=["Navya","Rajesh","Mahalya"]
name[2]="Mahalya Swarna"
print(name)

#insert

#syntax:variableName.insert(item)

name=[1,2,4,5]
name.insert(2,7)
print(name)

#append

lst=[]
lst.append("Navya")
print(lst)

#extend

#syntax:lst.extends(lst)

lst=["Navya","Rajesh"]
lst1=["Mallewari","Venkaiah"]
lst.extend(lst1)
print(lst)

#Delete

#Remove

#syntax:lst.remove(item)

name=["Navya","Mahalya","rajesh","Sitara"]
name.remove("Mahalya")
print(name)

#pop with index

#syntax:lst.pop(index)

name=["Navya","Mahalya","Rajesh"]
name.pop(2)
print(name)

#pop without index

#syntax:lst.pop()

name=["Navya","Mahalya","Rajesh","Aravind"]
name.pop()
print(name)



#clear

#syntax:lst.clear()

name=["Navya","Mahalya","Rajesh","Aravind"]
name.clear()
print(name)


#delete

#syntax:del variableName

name=["Navya","Mahalya","Rajesh","Aravind"]
del name[2]
print(name)

#input values

a=input("Enter a name:")
b=input("Enter a name:")
names=[]
names.append(a)
names.append(b)
print(names)


#sort

#syntax:lst.sort()

a=["Rose","Horse","Apple"]
a.sort()
print(a)

#without sort

a= [90,78,56,32,12,2]
n=len(a)
for i in range(0,n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)



#reverse

#syntax:lst.reverse()

a=["Rose","Horse","Apple"]
a.reverse()
print(a)


#Tuple

#implicit

#syntax:variableName=(item1,item2,...)

tpl=("eagle","monkey")
print(type(tpl))

#Explicit

#syntax:variableName=tpl((item1,item2,...))

tpl=tuple(("eagle","monkey"))
print(type(tpl))

#data type/Variable Annotation

#Syntax:variableName:tpl=((item1,item2,...)

tpl:tuple=(("eagle","monkey"))
print(type(tpl))

#tuple Methods

#Count,Index

#count

#syntax:tpl.count(item)

tpl=(("eagle","money","King","money"))
print(tpl.count("money"))

tpl=tuple((1,2,3,1))
print(tpl.count(1))

#index

#syntax:tpl.index(item)

tpl=tuple(("eagle","money","King"))
print(tpl.index("money"))


#conversion

tpl=tuple(("eagle","money","King"))
lst=list(tpl)
print(type(lst))


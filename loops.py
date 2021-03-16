#x=0
#while x<=5:
 #   print(x)
  #  x=x+1

counites_dict={}
counites_dict["Arapahoe"]=422829
counites_dict["Denver"]=463353
counites_dict["Jefferson"]=432438

for i,j in counites_dict.items():
#i==key, j==value
    print(i+" county has "+str(j)+" registered voters")

#Get the keys of a dictionary
for i in counites_dict:
    print(i)

for i in counites_dict.keys():
    print(i)

#Get the values of a dictionary

for i in counites_dict.values():
    print(i)

for i in counites_dict:
    print(counites_dict[i])

for i in counites_dict:
    print(counites_dict.get(i))
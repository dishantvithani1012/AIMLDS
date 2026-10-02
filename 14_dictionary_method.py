center ={'name':"The easy learn academy",'year':2014,'city':'bhavnagar','pincode':364001}

print(center)
center2= center.copy()
center2.clear()
print(center2)

del center2
print("keys",center.keys())
print("Values",center.values())

print("Dictionary as item ",center.items())

print("Institue name ",center.get('name',"Not found"))

print("institute email address ",center.get("email","not found"))

center.pop('pincode')
print(center)

center.popitem()
print(center)

#creating list

student =['name','age','gender','email','dob']

print(student)

#creating dictionary using list

dishant= dict.fromkeys(student)
sanket = dict.fromkeys(student)
kartik = dict.fromkeys(student)

print(student)

dishant ['name']= 'dishant vithani'
dishant ['age']=21
dishant ['gender']= 'Male'
print(dishant)
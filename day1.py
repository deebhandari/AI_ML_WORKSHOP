print("hello world") 
name ="ram"
print (f"hello,{name}!")

print("hello,"+ name +"!")

name = "ram"
faculty = "computer science"
dob = "01/11/2026"
# string concate 
print ("hello,"+name+""+"you are a studen to of"+faculty +"and your date of birth is " + dob)
# no concate
print (f"hello,{name}{faculty}{dob}")
# check data types
# Student Information Program

name = "Deepak"
faculty = "BCA"
dob = "2059-06-05"
age = 22

# Print values
print("Name:", name)
print("Faculty:", faculty)
print("Date of Birth:", dob)
print("Age:", age)

# Print data types
print(f"type of name: {type(name)}")
print(f"type of faculty: {type(faculty)}")
print(f"type of dob: {type(dob)}")
print(f"type of age: {type(age)}")
# swap variable easily
x, y = 10, 20

print("Before swap: x =", x, "y =", y)
print("After swap: x =", x, "y =", y)
      
    #   unpack lists
student_info =["charlese",21,88.0]
name, age,score = student_info
print("unpacked:",name,age,score)

# 

name1, age,score = student_info
print("unpacked:",name,age,score)

# creating list
student_names =["alice","bob","charlese","dino"]
student_scores =[85, 65, 95,90]

# accessing element (indexing starts at 0)
print("\n first elements:",student_names[0])
print("\n second elements:",student_names[-1])
print("\n three lements:",student_names[0:3])
print ("student from index 1 to and ",student_names[:])
print ("every second student :",)

student_names.append("eva") 
print ("\nafter adding eva:",student_names)


student_names.insert("1,frank:")
print("\after instering frank",student_names)

student_names.removed("bob")
print("after removing :",student_names)


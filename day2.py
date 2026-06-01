#tuples are similar to lists but are immutable (cannot be changed after cretion)

#tuples cannot to change after creation
student_record =["alice" ,20,85,3,"computer science"]
print ("student record tuples",student_record)
#accessing tuples elements
print ("name",student_record)
print("age",student_record)

course_A ={"alice","bob","charlese","banana"}
course_B ={"charles", "dina","bob","nukesh"}

print ("course A students:", course_A)
print ("course A students:", course_B)
#set operations grat for finding  ovrer laps)
print ("\nstudent in both courses",course_A & course_B)
print("\nstudent in either course",course_A |course_B )
print("\nstudent in only A:",course_A - course_B )
print("\nstudent in only B:",course_A & course_B )
print("only in one course :",course_A ^ course_B )

#remove duplications from list using set
score_with_duplicates =[85, 56,77,77,71, 22, 88,44,11]
unique_scores = list(score_with_duplicates)
print("unique scores:",unique_scores)

print("\n --Dictonaries ---")
print ("="*50)

#dictionary score store key - value pairs and are very useful for structured data
#dictionary data with key
student = {
 'name': 'Alice',
 'age': 22,
 'scores': [25, 28, 44,100],
 'department': 'BCA',
 'hobbies' : ['dance, singing, social workers, programming,writing'],
 'is_active': True
}
print ("student dictonary")
print (student)

#accessing values
print("\n student name:", student["name"])
print("\n student scores:", student["scores"])

average = sum(student["scores"]) / len(student["scores"])
print("average scores:", average)

print("scores greater than 80:")

for score in student["scores"]:
    if score > 80:
        print(score)
        
        
        #add and update value
        student['grade'] = "A"
        student['age'] = 21
        student['hobbies'] =['dancing','singing'],
        
        
        print("\n after upadtes:",student)
        
        alice_score = student["scores"]
        alice_passing_scores = [score for score in alice_score if score >=80 ]
        print("\n  alice passing (>=80):",alice_passing_scores)
        
        #condition statements 
        #function to determine grade before on score 
        
    def get_grade(score):
        if score >= 90:
           return "A"
        elif score >= 80:
           return "B"
        elif score >= 70:
         return "C"
        elif score >= 60:
         return "D"
        else:
          return "F"


# TEST THE FUNCTION
test_scores = [45, 60, 90, 40, 100]

for score in test_scores:
    grade = get_grade(score)
    print("Score:", score, "Grade:", grade)
 








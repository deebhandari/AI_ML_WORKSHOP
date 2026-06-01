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

print ("\nstudent in both courses",course_A & course_B)
print("\nstudent in either course",course_A |course_B )
print("\nstudent in only A:",course_A - course_B )
print("\nstudent in only B:",course_A & course_B )
print("only in one course :",course_A ^ course_B )


score_with_duplicates =[85, 56,77,77,71, 22, 88,44,11]
unique_scores = list(score_with_duplicates)
print("unique scores:",unique_scores)


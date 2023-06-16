try:
    file_write = open(r"C:\Users\kolov\[ Python ]  Assignment\Student_Score\score.txt","w")
    while True:
        student_id = input("Please enter the student id :")
        if student_id == 'exit':
            break
        score = input("Please enter student score : ")
        file_write.writelines(student_id+'\t'+score+'\n')
    file_write.close()
    
    file_read = open(r"C:\Users\kolov\[ Python ]  Assignment\Student_Score\score.txt","r",encoding="utf-8")
    file_write = open(r"C:\Users\kolov\[ Python ]  Assignment\Student_Score\grade.txt","w")
    for line in file_read.readlines():
        score = line[-4:].strip() #student score
        student_id = line[:-4].strip() #student id
        score = int(score)
        if score >= 80 and score <= 100:
            grade = 'A'
        if score >= 70 and score <= 79:
            grade = 'B'
        if score >= 60 and score <= 69:
            grade = 'C'
        if score >= 50 and score <= 59:
            grade = 'D'
        if score >= 0 and score <= 49:
            grade = 'F'
        # print("Student_ID : ",student_id,"Score : ",str(score),"Grade : ",grade)
        file_write.writelines("Student_ID : "+student_id+" Score : "+str(score)+" Grade : "+grade+'\n')
    file_write.close()
    file_read.close()
except Exception as e:
    print(e)
    
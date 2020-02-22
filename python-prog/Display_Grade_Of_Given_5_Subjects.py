#Python Program to Take in the Marks of 5 Subjects and Display the Grade

#subjectList = [int(input("enter subject %d : "%i)) for i in range(1,int(input("enter n value : "))+1)]
#print(subjectList)

getSubjectList = lambda msg1, msg2 : [int(input("{} : ".format(msg1)%i)) for i in range(1,int(input("{} : ".format(msg2)))+1)]

def getGrade(subjectList) :
    '''return grade of given list, parameter is list of subjects score'''
    grade = ''
    avgScore = sum(subjectList)/len(subjectList)
    if avgScore >= 90 :
        grade = 'A'
    elif avgScore >= 80 and avgScore < 90 :
        grade = 'B'
    elif avgScore >= 70 and avgScore < 80 :
        grade = 'C'
    elif avgScore >= 60 and avgScore < 70 :
        grade = 'D'
    else :
        grade = 'F'
    return grade

def cal_grade() :
    try :
        subjectMarksList = getSubjectList('enter subject %d marks','How many Subjects would like to calucate grade')
        grade = getGrade(subjectMarksList)
        print('Grade is %s'%grade)
    except(ValueError,ZeroDivisionError)  as ex :
        print(ex)
    except Exception as ex :
        print(ex)
    except Error as err :
        print(err)
    
cal_grade()
          


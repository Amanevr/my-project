import sys

welcomestring="welcome to DSIT "
welcomestring=welcomestring.center(80,"*")
print(welcomestring)
student_category=0
employee_category=0
unemployee_category=0
pass_number=0

total_participant_dict={}
maxpartlimit=int(input("enter the participant limit:"))

for i in range(1,maxpartlimit+1):
    participantname=input("enter the participant name:")
    place=input("enter the place:")
    category=input("enter the category(S/E/UE):")
    print("your pass number is:",pass_number)
    print("your participanr name is:",participantname)
    print("place:",place)
    print("category:",category)
    i=i+1

print("house full only",maxpartlimit,"participant are alllowed for seminar")
print(total_participant_dict)

choice=input("do you want report? press yes , otherwise press any key")
if choice == "yes":
    for keys,values in total_participant_dict.items():
        if total_participant_dict[keys]["category"]=="student":
            student_category=student_category+1
        elif total_participant_dict[keys]["category"]=="employee":
            employee_category=employee_category+1
        elif total_participant_dict[keys]["category"]=="unemployee":
            unemployee_category=unemployee_category+1
    print("************Data science********")
    print("****************evr**************")
    print("*********seminar*****************")
    print("**********report*****************")
    total_participant_dict=student_category+employee_category+unemployee_category
    print("total number of participant:                    :",total_participant_dict)
    print("total number of student attendance in seminr    :",student_category)
    print("total number of employee attendance in seminr   :",employee_category)
    print("total number of unemployee attendance in seminr :",unemployee_category)
else:
    print("thank you")
    sys.exit()


'''
Library Management System
developed By: UJJWAL KUMAR PRANAMI
'''

liblog = "liblog.txt"
userdata = "userdata.txt"
bookdata = "bookdata.txt"
studentdata = "studentdata.txt"
issue_return = "issue_return.txt"
import os
from datetime import date
today=date.today()
todaydate = today.strftime("%d/%m/%Y")
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#setup of library management system for the first time
try:
    f = open( liblog )
    # Do something with the file
except IOError:
    open( liblog, "x")
    open( userdata, "x")
    open( bookdata, "x")
    open( studentdata, "x")
    open( issue_return,"x")
    lib=open( liblog, "r")
    if lib.readline() == '':
        lib.close()
        print("Welcome \r")
        print("Please Sign Up")
        user = input("User ID:")
        userpass = input("Password:")
        newusr = open( userdata, "w")
        lib = open( liblog, "w")
        newusr.write(f"{user}<{userpass}>\n")
        print("Signed Up Sucessfully")
        lib.write(f"{user}-{current_time}[{todaydate}]\n")
        newusr.close()
    lib.close()
  
#Main code start from here
def feedlog( usr ):
    lib = open( liblog, "a")
    lib.write(f"{usr}-{current_time}[{todaydate}]\n")
    lib.close()

    
def addbook( isbn, bnm):
    f = open( bookdata, "a")
    f.write(f"{isbn}-{bnm}\n")
    print("Book Added Sucessfully")
    f.close()
    input()


def addstudent( sid, snm):
    f = open( studentdata, "a")
    f.write(f"{sid}-{snm}\n")
    print("Student Added Sucessfully")
    f.close()
    input()


def adduser( usr, pas):
    f = open( userdata, "a")
    f.write(f"{usr}<{pas}>\n")
    print("User Added Sucessfully")
    f.close()
    input()


def checkuser( usr, pas):
    f = open( userdata,"r")
    x = f.readline()
    tusr = ""
    for i in x: 
        if i =="<":
            if usr == tusr:
                tpass = ""
                for j in range(-6, -2, 1):
                    tpass = tpass + x[j]
                if pas == tpass:
                    f.close()
                    return 101
                else:
                    print("Wrong Master User Password")
                    input()
            break
        else:
            tusr = tusr + i
    f.close()
    return 1


def searchbook( isbn ):
    f=open( bookdata, "r")
    for x in f.readlines():
        tempisbn =  ""
        for i in x:
            if i == "-":
                if isbn == tempisbn:
                    f.close()
                    bnm=x[11:]
                    bnm=bnm.strip(("\n"))
                    return bnm
                break
            else:
                tempisbn = tempisbn + i
    f.close()
    return 1


def searchstudent( sid ):
    f = open( studentdata, "r")
    for x in f.readlines():
        tempsid = ""
        for i in x:
            if i == "-":
                if sid == tempsid:
                    snm = x[13:]
                    snm = snm.strip("\n")
                    f.close()
                    return x[13:]
                break
            else:
                tempsid = tempsid + i
    f.close()
    return 1


def searchuser( usr ):
    f = open( userdata, "r")
    for x in f.readlines():
        tempusr = ""
        for i in x:
            if i == "<":
                if usr == tempusr:
                    pas=x[-6:-2]
                    f.close()
                    return pas
                break
            else:
                tempusr=tempusr+i
    f.close()
    return 1


def showstudentdetails(sid):
    print("Student Details")
    print(f"Student ID:{sid} \tName:{searchstudent( sid )} \n---Book Details---") 
    f = open( issue_return, "r")
    j=1
    for x in f.readlines():
        tempsid = ""
        for i in x:
            if i == "-":
                if sid == tempsid:
                    isbn = x[13:23]
                    d1 = x[25:35]
                    d1 = d1.strip("\n")
                    print(f"({j}).Book ISBN:{isbn} \tBook Name:{searchbook( isbn )} \tIssue Date:{d1}\r")
                    j+=1
                break
            else:
                tempsid = tempsid + i                    
    f.close()
    input()


def issue( sid, isbn):
    f = open( issue_return, "a")
    f.write(f"{sid}-{isbn}-[{todaydate}]\n")
    print("Issued sucessfully\n\n")
    f.close()
    showstudentdetails( sid )


def ret( sid, isbn):
    numberofline = 0
    fread = open( issue_return, "r")
    for x in fread.readlines():
        tempsid = ""
        for i in x:
            if i == "-":
                if sid == tempsid:
                    tempisbn = x[13:23]
                    tempisbn = tempisbn.strip("\n")
                    if isbn == tempisbn:
                        issuedate=x[25:27]
                        issuemonth=x[28:30]
                        issueyear=x[31:35]
                        d1=todaydate[:2]
                        m1=todaydate[3:5]
                        y1=todaydate[6:10]
                        fread.close()
                        fine=0
                        if issueyear == y1:
                            if issuemonth == m1:
                                if int(issuedate)+15 >=int(d1):
                                    fine=0
                                else:
                                    fine=int(d1)-(int(issuedate+15))
                            else:
                                fine=(int(m1)-int(issuemonth))*28
                        else:
                            fine=(int(y1)-int(issueyear))*336
                        
                        if fine != 0:
                            print(f"Your fine is:{fine}")
                            if input("Want to return:(y/n):") == 'n':
                                print("Book not returned due to FINE NOT SUBMITTED")
                                input()
                                return

                        fread = open( issue_return, "r")
                        contentline = fread.readlines()
                        fread.close()
                        contentline.pop( numberofline )
                        freset = open( issue_return, "w")
                        freset.close()
                        fwrite = open( issue_return, "a")
                        for index in contentline:
                            index = index.strip("'\n")
                            fwrite.write(index + "\n")
                        fwrite.close()
                        print("Book Returned Sucessfully\n\n")
                        showstudentdetails(sid)
                break
            else:
                tempsid = tempsid + i
        numberofline = numberofline + 1
    fread.close()

def checksid( sid ):
    if len(sid) == 12:
        return 0
    else:
        return 1


def checkisbn( isbn ):
    if len(isbn) == 10:
        return 0
    else:
        return 1


#Main Login
if __name__ == '__main__':
    print("\t\t\t\t\t\tPlease login")
    usr = input("\t\t\t\t\tUser ID:")
    if searchuser( usr ) == 1:
        print("\t\t\t\t\tUser Not Found")
        input()
    else:   
        feedlog( usr )
        pas = input("\t\t\t\t\tPassword: ")
        if pas == searchuser(usr):
            #login sucessfully
            print("Login Sucessfully \r")
            c = 99
            while (c != 0):
                os.system('cls')
                print("Welcome TO LIBRARY MANAGEMENT SYSTEM")
                print("Operations \r")
                print("1. Add Book \r")
                print("2. Add Student \r")
                print("3. Add User \r")
                print("4. Issue Book \r")
                print("5. Return Book \r")
                print("6. Search Book \r")
                print("7. Search Student \r")
                print("8. Search User \r")
                print("9. Student Detail \r")
                print("0. Exit \r")
                c = int(input("Your Choice: "))
                if c == 0:
                    print(f"Thankyou {usr}, for using our software")
                 
                elif c == 1:
                    os.system('cls')
                    print("Add New Book")
                    bnm = input("Enter the name of Book:")
                    isbn = input("Enter ISBN code:")
                    if checkisbn(isbn) == 0:
                        addbook( isbn, bnm)
                    else:
                        print("Short ISBN\rISBN number must be of 10 character(ex-1234567890)")
                        input()

                elif c == 2:
                    os.system('cls')
                    print("Add New Student")
                    snm=input("Enter the name of Student:")
                    sid=input("Enter Student ID:")
                    if checksid( sid ) == 0:
                        addstudent( sid, snm)                    
                    else:
                        print("Short Student ID\rStudent ID number must be of 12 character(ex-0126CS191XXX)")
                        input()

                elif c == 3:
                    os.system('cls')
                    print("Add New User")
                    usr = input("Enter Master User ID:")
                    pas = input("Password:")
                    check = checkuser( usr, pas)
                    if check == 101:
                        print(f"Welcome {usr}")
                        usr = input("Enter New User ID:")
                        pas = input("Password:")
                        adduser( usr, pas)
                        print("User Added Sucessfully")
                    else:
                        print("Master User ID or Password not mached")
                        print("New User Cannot Be Added")
                        input()

                elif c == 4:
                    os.system('cls')
                    print("Issue Book")
                    sid = input("Enter Student ID:")
                    if checksid( sid ) == 0:
                        if searchstudent( sid ) != 1:
                            isbn = input("Enter ISBN code:")                        
                            if checkisbn( isbn ) == 0:
                                if searchbook( isbn ) != 1:
                                    issue( sid, isbn)
                                else:
                                    print("Book Not Found")
                                    input()
                            else:
                                print("Short ISBN\rISBN number must be of 10 character(ex-1234567890)")
                                input()
                        else:
                            print("Student Not Found")
                            input()
                    else:
                        print("Short Student ID\rStudent ID number must be of 12 character(ex-0126CS191XXX)")
                        input()
                            
                elif c == 5:
                    os.system('cls')
                    print("Return Book")
                    sid = input("Enter Student ID:")
                    if checksid( sid ) == 0:
                        if searchstudent( sid ) != 1:
                            isbn=input("Enter ISBN code:")                        
                            if checkisbn( isbn ) == 0:
                                if searchbook( isbn ) != 1:
                                    ret( sid, isbn)
                                else:
                                    print("Book Not Found")
                                    input()
                            else:
                                print("Short ISBN\rISBN number must be of 10 character(ex-1234567890)")
                                input()
                        else:
                            print("Student Not Found")
                            input()
                    else:
                        print("Short Student ID\rStudent ID number must be of 12 character(ex-0126CS191XXX)")
                        input()

                elif c == 6:
                    os.system('cls')
                    print("Search Book")
                    isbn = input("Enter ISBN:")
                    if checkisbn(isbn) == 0:
                        if searchbook(isbn) != 1:
                            print("Book Found \r")
                            print(f"Book:{searchbook(isbn)}        ISBN:{isbn}")
                            input()
                        else:
                            print("Book Not found")
                            input()
                    else:   
                        print("Short ISBN\rISBN number must be of 10 character(ex-1234567890)")
                        input()

                elif c == 7:
                    os.system('cls')
                    print("Search Student")
                    sid = input("Enter Student ID:")
                    if checksid(sid) == 0:
                        if searchstudent(sid) != 1:
                            print("Student Found \r")
                            print(f"Student ID:{sid}")
                            print(f"Name:{searchstudent(sid)}",end='')
                            input()
                        else:
                            print("Student Not Found")
                            input()
                    else:
                        print("Short Student ID\rStudent ID number must be of 12 character(ex-0126CS191XXX)")
                        input()
                              
                elif c == 8:
                    os.system('cls')
                    print("Search User")
                    tempusr = input("Enter User ID:")
                    if searchuser(tempusr) == 1:
                        print("User Not Found")
                        input()
                    else:
                        print("User Found")
                        input()
                            
                elif c == 9:
                    os.system('cls')
                    print("Find Student Details")
                    sid = input("Enter Student ID:")
                    if checksid(sid) == 0:
                        if searchstudent(sid) != 1:
                            print(showstudentdetails(sid))
                        else:
                            print("STUDENT NOT FOUND")
                            input()
                    else:
                        print("Short Student ID\rStudent ID number must be of 12 character(ex-0126CS191XXX)")
                        input()

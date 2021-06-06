SETUP
1: Ask for Sign Up(user ID(MASTER USER ID) and Password )
	//Ask for sign up only when program run for first time in other device
2:Login Page(Login through user id and password)
	//Everytime it ask for login
3:TAKE INPUTS AS FOLLOW:
	USER ID- Ujjwal,nishu,PAPA,bhailog,etc[string without whitespace] 
	PASSWORD- 1234,A12C,abcd,B12c,etc[fourr digit numeric pin]
		//MUST BE 4 CHARACTER OTHERWISE IT'LL NOT ACCEPT	
	STUDENT ID- 0126CS191111,0126CS191000,0126CS191096,e.t.c[12 char]
		//MUST BE 12 CHARACTER OTHERWISE IT'LL NOT ACCEPT	
	ISBN NO.- 1234567890,1234543210,1234509876,e.t.c[10 char only]
		//MUST BE 10 CHARACTER OTHERWISE IT'LL NOT ACCEPT
4:PROVIDED OPERATIONS
	1. Add Book - add new book details(isbn,bookname) to bookdata.txt
                  2. Add Student - add new Student (sID,studentname) to studentdata.txt
                  3. Add User - add new user details(user ID,password) to userdata.txt
                  4. Issue Book - add (StudentID-ISBN) into issue_return.txt
                  5. Return Book - remove (StudentID-ISBN) into issue_return.txt
                  6. Search Book - search for ISBN in bookdata.txt
                  7. Search Student - search Student ID in student.txt
                  8. Search User - search User in userdata.txt
                  9. Student Detail - show student details(name,SID,Book owned)
                  0. Exit - To EXIT
5:TOTAL NUMBER OF FILES:5
	A>userdata.txt{Pranami<1234>}
			^             ^   
	 	           USERID    PASSWORD	
	B>studentdata.txt{0126CS191096-Sahil Ahuja}
			       ^		^
			STUDENT ID           STUDENT NAME
	C>bookdata.txt{1234567890-Python}
			    ^	     ^
			ISBN         BOOK NAME
	D>issue_return.txt{0126CS191096-1234567890}
			           ^                          ^
               			   STUDENT ID        	ISBN
	E>liblog.txt{Pranami-12:30:30}	
		          ^          ^    ^    ^
		      user       H    M   S->TIME	
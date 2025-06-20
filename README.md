# Webapplication-security

This Python scripts tells about the web vulnerability->Sql injection and cross site scripting(xss).This project uses Python's Flask package which is used to build  small APIs,and SQLite,bleach.

Task 1:
     The first task is all about how the Sql injection occurs and how it can be prevented.It contains two logins the first one is Vulnerable to sql injection and the other one is secure.In the vulnerable login the attacker can inject the malicious Sql Query and can get  access to all the datas in the database.This occurs more commonly due to poor api design and it can be prevented by using SQLAlchemy ORM which sanitizes the input.Due to the implementation of this security control even if the threat actor enters the malicious sql query it don't retrieve the data from the database.

     
Task 2:
     The second task tells about one of the OWASP(Top 10) web vulnerability that is XSS(cross site scripting).This attack occurs due to the poor api design.This attack occurs by entering the malicious javascript code into the any field like comments after the threat actor enters the code it saves into the web server.when a user visites the webpage the server gets the request and the entire code(also the malicious code)is executed.By exploiting this vulnerability the threat actor can steal the victim's session token,can redirect to any other vulnerable website etc.. . it can be prevented by sanitizing user input using bleach(a python package)which sanitizes the user input.

     
Packages used:
      >Flask
      >SQLite (SQLAlchemy)
      >bleach (for input sanitization in XSS demo)

      
Sample Output:

Task 1:
   ![Screenshot (58)](https://github.com/user-attachments/assets/4b1752c6-ff8b-4a2f-be96-1a61e6c6f001)
   ![Screenshot (59)](https://github.com/user-attachments/assets/127c1fd7-c8f0-4dda-88bc-8afeb8310456)
   ![Screenshot (60)](https://github.com/user-attachments/assets/4ac4694e-2777-463e-b25a-6712387156e9)
   ![Screenshot (61)](https://github.com/user-attachments/assets/0fd7e986-409f-43df-a3fd-205435309364)
   
Task 2:
   ![Screenshot (62)](https://github.com/user-attachments/assets/82884daa-300c-4952-8955-91fee87fe257)
   ![Screenshot (63)](https://github.com/user-attachments/assets/2a3548ca-1307-478f-b3ab-0aca38e04dbf)
   ![Screenshot (64)](https://github.com/user-attachments/assets/dde81a36-b5d7-4cc8-bc95-4e94bf45286c)
   ![Screenshot (65)](https://github.com/user-attachments/assets/f41e82c1-b964-4d24-8ece-8dc04ded8a43)



   





# Client_Management_Application
A form is created taking the user input and storing the information in the database.
The form has been created in on the Django flatform.

Various information such as 
Client ID, 
First name, 
Last name, 
Email, 
Phone number, 
Business name, 
Bank account number, 
Address (Street1, Street2, City, State, Country, pincode), 
status ( 'Active', 'passive', 'pipeline', 'prospect’) 
have been taken as input.

API endpoints implementing the application feature of Django is under hood of implementation of this form.


Procedure of reaching this final application:

1) Initiated a project start.
2) Created a project application
3) Python script for the variable inputs for the information mentioned above.
4) View creation handling the html and the python data files according to the request methods(POST,GET,DELETE)
5) Creating a html script, implementing the design of the fields and template creation.


The project is built in Ubuntu 15.04.

*Django installment is the prerequisite for the project to work in Ubuntu*
Direction to run on Linux:

1) Navigate into the folder through CommandLine  "Client_Management_Application"
2) Type - "python manage.py runserver"
3) Go to the browser and enter "http://127.0.0.1:8000/signup/"

A Data entry page will pop-up(pic_1 as mentioned in the photos folder).
Submit button for now will direct to another html page displaying the data entered in the previous page.

# WORLD PHONE LIST
#### Video Demo:  [<https://youtu.be/GJtBWlH8cro>]
![WordPhoneList](https://user-images.githubusercontent.com/100033559/216462577-14c06db9-9fef-4e3e-b47e-238d4663faf0.gif)

#### Description:

 For this project, I used:

 - Flask as a framework:
    Flask was used, to get user input from our HTML, I also used flask_session to remember the user

 - Python as the language for the internal process:
    Python was used to make user interaction with our database and page interaction.

 - HTML and CSS:
    HTML and CSS were used to generate the static page

 - And the database used was SQLite3:
    In sqlite3 we create 2 tables, one for the user, and another to store the user's name and number

The initial idea of this project is that it can help family members who have lost contact with other family members,
since the application only delivers what is promised if you know the full name of the person you are looking for... And of course,
if they are already registered in the app.

For this, the application checks if the name exists in our database, if it exists, the application returns a list,
with the name and phone number of the person sought.

To access the search field, the person must first login, if they do not have an account,
they must first register, with full name, e-mail, telephone number and password.

If the email already exists in our database, it will return an error to the user, stating that the user's email already exists...

In the input for the name, I forced all characters to uppercase so we don't have problems in the search field!

in the email entry I forced all characters to lowercase.

Inside the database, two tables were built, one with the user's name,
to store user data such as id, email and password, and another with the name of the contacts to store the id, phone and full name.

- Login:

![github-small](/imgs/projeto-login.PNG)
    - On the Login page, it is checked if the user exists in our database, if it exists,
      it is redirected to a list, if it does not exist, it is redirected to an ERROR screen
    - User input for email is forced to lowercase.
    - In the input for name, we force the characters to uppercase

- Register:

![github-small](/imgs/projeto-register.PNG)
    - In register, it is also checked if the user already exists in our database, if it not exists, it is redirected to an error message, otherwise it is redirected to a list
    - In the email input, we force the characters to lowercase.
    - In the input for name, we force the characters to uppercase
    - User's full name is required for registration
    - We have a password field and a password confirmation field.
    - Check if the passwords match

- Search:

![github-small](/imgs/projeto-busca.PNG)
    - In the search field, the full name of the person the user is looking for is requested.
    - Check if the user exists in our database
    - If it exists, it is redirected to a list.
    - Otherwise, you are redirected to an error message.

- List:

![github-small](/imgs/projeto-list.PNG)
    - A table is shown in the list, this table contains the number and name of the person being searched for!

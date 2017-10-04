from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
#    return form.format(error_password='',error_name='',error_pass_same='')
    return render_template('homepage.html')

@app.route("/",methods=['POST'])
def validate_login():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    error_name=""
    error_password=""
    error_pass_same=""
    email_error=""
    password1=""

    
    if password == "":
       error_password = "'{0}'please specify the password".format(password)
       password=""
    else:
        if len(password) > 20:
           error_password = "password lenght is more than 20 Characters"
           password1=password
           password = ""
        else:
            if len(password) < 3:
              error_password = "password is less than 3 characters"
              password1=password
              password=""
            else:
              password = password
    if verify == "":
       error_pass_same = "'{0}'password re-enter is empty".format(verify)
       verify=""
       password=""
    else:
        if verify != password:
           if password1 == verify : 
              verify =""
              password=""
           else:
              error_pass_same = "Password did not match "
              verify =""
              password=""
        else:
            if verify == password : 
               if password1 != "" :
                   password = ""
                   verify = ""
    if password == "":
        verify = ""
    else:
        verify = verify
    if email != "" :
        if " " in email :
            email_error = "entered email has spaces or wrong email "
            email=""
            password=""
            verify=""
        else: 
           if len(email) < 3 or len(email) > 20 :
              email_error = "entered email is less then 3 char or more than 20 Char "
              email=""
              password=""
              Verify=""
           else:
              if "@" in email and "." in email :
                    email = email
              else:
                 email_error = "entered wrong email address "
                 email=""
                 password=""
                 verify=""


    if email == "":
        email = email
    
    if username == "":
       error_name = "'{0}'please specify the username".format(username)
       username=""
       
    else:
        if len(username) > 20:
           error_name = "username should not be more than 20 characters"
           username=""
           
        else:
            if len(username) < 3 :
               error_name = "username should be min 3 letters"
               username=""
               
            else:
                username = username
    
    if not error_name and not error_password and not error_pass_same and not email_error :
        return render_template('templates.html',username=username)
    else:    
        return render_template('homepage.html',
            username=username,
            password=password,
            verify=verify,
            email=email,
            error_name=error_name,
            error_password=error_password,
            error_pass_same=error_pass_same,
            email_error=email_error)
app.run()


from flask import Flask, request, redirect, render_template



app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/" , methods=['POST','GET'])
def index():
    username = ''
    username_err = ''
    password = ''
    vpassword = ''
    email = ''
    email_err = ''
    password_err = ''
    vpassword_err = ''

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        vpassword = request.form['vpassword']
        email = request.form['email']

        for i in username:
            if i.isspace():
                username_err = 'Username must have no spaces'
                
            else:
                if (len(username)) < 3 or (len(username) > 20):
                    username_err = "Username must be within 3-20 characters."
                    
        if not empty_input(username):
            username_err = 'Please input a username'
            

        for i in password:
            if i.isspace():
                password_err = 'Password must have no spaces'
            else:
                if (len(password) < 3) or (len(password) > 20):
                    password_err = "Password must be within 3-20 characters."
                    password = ''
        
        if not empty_input(password):
            password_err = 'Please input a password'
            password = ''
            

        if password != vpassword:
            vpassword_err = 'Passwords do not match.'
            vpassword = ''
            password_err = 'Passwords do not match.'
            password = ''
        
        for i in email:
            if i.isspace():
                email_err = 'Email must have no spaces'
            else:
                if (len(email)) < 3 or (len(email) > 20):
                    email_err = "Email must be within 3-20 characters."

        if email_at(email):
            email_err = 'Too many @ symbols'
            email = ''

        if email_period(email):
            email_err = 'Too many . symbols'
            email = ''



        if (not username_err) and (not password_err) and (not vpassword_err) and (not email_err):
            return redirect('/welcome?username={0}'.format(username))
                
        


    
    return render_template('signup.html', username=username, password=password,
    vpassword=vpassword, email=email,username_err=username_err,password_err=password_err,vpassword_err=vpassword_err,email_err=email_err)

@app.route("/welcome")
def welcome():
    title = "Welcome"
    username = request.args.get('username')
    return render_template('welcome.html', username=username, title=title)


def empty_input(x):
    if x:
        return True
    else:
        return False

def email_at(x):
    if x.count('@') > 1:
        return True
    else:
        return False

def email_period(x):
    if x.count('.') > 1:
        return True
    else:
        return False




app.run()



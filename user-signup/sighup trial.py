from flask import Flask,render_template,request, redirect


app=Flask(__name__)
app.config['DEBUG']=True



@app.route("/homepage")
def index():  
  #return form.format("")
  return render_template('homepage.html')

@app.route('/signUp',methods=['POST'])
def signUp():
	_name = request.form['username']
	_email = request.form['email']
	_password = request.form['password']
	_verify = request.form['verify']

   if _name and _email and _password:    	
	
@app.route('/validate-signup' ,methods=['POST'])	
def validate-signup():
    return homepage.format(signup='',password='',verify='',email='')
	

  
  
app.run()


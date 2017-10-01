from flask import Flask,render_template,request, redirect


app=Flask(__name__)
app.config['DEBUG']=True



@app.route("/")
def index():  
  #return form.format("")
  return render_template('homepage.html')

app.run()


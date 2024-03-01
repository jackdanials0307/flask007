from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)

@app.route('/')
def landing():
     return render_template('landing.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        if request.form['uname']!='admin' or request.form['pass']!='admin':
            err="invalid"
        else:
            return redirect(url_for('home'))
        
    return render_template('login.html',err=err)
        

# host
if __name__=='__main__':
    app.run()
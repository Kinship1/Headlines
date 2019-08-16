from flask import Flask,request,render_template
from flask import session,redirect
import time
import subprocess
import pandas as pd

app = Flask(__name__)
app.secret_key = 'flaskmysavior'
types = ""

@app.route('/',methods=['GET','POST'])
def home():
        return render_template('home.html')



@app.route('/news',methods=['GET','POST'])
def news():
        if request.method == 'POST':
                global types  
                types = request.form.get('TypeOfNew')
                file1 = open("type.txt","w")
                file1.write(types)
                file1.close()
                subprocess.call("python soupy1.py")
                return render_template('mypage.html')


if __name__ == "__main__":
        app.run(debug=True)

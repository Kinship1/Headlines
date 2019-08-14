from flask import Flask,request,render_template
from flask import session,redirect
import time
import subprocess


app = Flask(__name__)
app.secret_key = 'flaskmysavior'

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')


@app.route('/news',methods=['GET','POST'])
def news():
    if request.method == 'POST':
        global types = request.form.get('TypeOfNew')
        subprocess.call("python soupy1.py")
        print(types)   
        return render_template('mypage.html')

if __name__ == "__main__":
    # scrapy runspider snapdeal.py -a value=laptop -o snap.csv
    app.run(debug=True)


from flask import Flask, render_template, request, session, redirect, url_for



app = Flask(__name__)

app.secret_key='12345678'

courses = [
{
    "id":"20TS1234",
    "name":"PFSD",
    "LTPS": "0-0-0-8",
    "credits":4

},
{
    "id":"20CNS9876",
    "name": "CNS",
    "LTPS": "4-0-4-0",
    "credits": 4
},
{
    "id":"20AI9876",
    "name": "AIDS",
    "LTPS": "4-0-4-0",
    "credits": 4
}
]

grade = [
    {
        "image": "https://newerp.kluniversity.in/uploads/student_photo/39906.jpg",
        "name":"Mohan Sai Teja",
        "subject": "MP-2",
        "marks": 70,
        "status":"promoted",
        "remarks":"Average"
    },
    {
        "image": "https://www.jbpainting.com.au/wp-content/uploads/2016/08/gravatar-m.jpg",
        "name":"M Prem Chandu",
        "subject": "DAA",
        "marks": 90,
        "status":"promoted",
        "remarks":"Good",
    },
    {
        "image": "https://www.jbpainting.com.au/wp-content/uploads/2016/08/gravatar-m.jpg",
        "name":"V Charan Sai",
        "subject": "DAA",
        "marks": 80,
        "status":"Promoted",
        "remarks":"Good"
    }
]





@app.route('/')
def home():
    login=False
    if 'username' in session:
        login=True
    return render_template("home.html", title="Home",login=login)

@app.route('/courses')
def subject():
    login=False
    if 'username' in session:
        login=True
    return render_template("courses.html", title="Courses",courses=courses,login=login)

@app.route('/submissions')
def submissions():
    login=False
    if 'username' in session:
        login=True
    return render_template("submissions.html", title="Submissions",login=login)

@app.route('/grades')
def grades():
    login=False
    if 'username' in session:
        login=True
    return render_template("grades.html", title="Grades",grades=grade,login=login)

@app.route('/contact')
def contact():
    login=False
    if 'username' in session:
        login=True
    return render_template("contact.html", title="Contact",login=login)

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return render_template("login.html", title="Login Page")

@app.route("/logout")
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))



if __name__=="__main__":
    app.run(debug=True)

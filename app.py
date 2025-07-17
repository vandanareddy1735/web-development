from flask import Flask, render_template, redirect, url_for, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your actual MySQL username
        password='',  # Replace with your actual MySQL password
        database='employer'
    )
    return connection


@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET'])
def dashboardsignup():
    return render_template("dashboardsignup.html")

@app.route('/forgotpassword', methods=['GET'])
def sendotp():
    return render_template("forgot password.html")

@app.route('/employersignup', methods=['GET', 'POST'])
def employersignup():
    if request.method == 'POST':
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        
        if password == confirm_password:
            return redirect(url_for('emailverificationforsignup'))
        else:
            return redirect(url_for('employersignup'))
    
    return render_template("employer signup.html")

@app.route('/employersignupb', methods=['GET'])
def employersignupb():
    return redirect(url_for('employersignup'))

@app.route('/employeesignup', methods=['GET', 'POST'])
def employeesignup():
    if request.method == 'POST':
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        
        if password == confirm_password:
            return redirect(url_for('emailverificationforsignup'))
        else:
            return redirect(url_for('employeesignup'))
    
    return render_template("signup.html")

@app.route('/employeesignupb', methods=['GET'])
def signupb():
    return redirect(url_for('employeesignup'))

@app.route('/newpassword', methods=['GET'])
def newpasswordp():
    return render_template("new password.html")

@app.route('/newpasswordp', methods=['POST'])
def newpassword():
    otp = ''.join([request.form.get(f'otp{i}') for i in range(1, 7)])
    if len(otp) == 6 and otp.isdigit():
        return redirect(url_for('newpasswordp'))
    else:
        return redirect(url_for('emailverification'))

@app.route('/resetpassword', methods=['POST'])
def resetpassword():
    new_password = request.form['newPassword']
    confirm_password = request.form['confirmPassword']
    
    if new_password and new_password == confirm_password:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('newpasswordp'))



@app.route('/companies')
def companiesb():
    return render_template('companies.html')

@app.route('/companiesb', methods=['GET'])
def companies():
    return redirect(url_for('companiesb'))

@app.route('/jobs')
def jobsb():
    return render_template('jobs.html')

@app.route('/jobsb', methods=['GET'])
def jobs():
    return redirect(url_for('jobsb'))

@app.route('/services')
def servicesb():
    return render_template('services.html')

@app.route('/servicesb', methods=['GET'])
def services():
    return redirect(url_for('servicesb'))

@app.route('/contactus')
def contactusb():
    return render_template("contact.html")

@app.route('/employercontactus')
def contactus():
    return render_template("contactus.html")

@app.route('/feedback')
def feedback():
    return render_template("feedback.html")

@app.route('/email')
def email():
    return redirect(url_for('emailverification'))

@app.route('/emailverification')
def emailverification():
    return render_template("email.html")

@app.route('/emailforsignup')
def emailforsignup():
    return redirect(url_for('emailverificationforsignup'))

@app.route('/emailverificationforsignup', methods=['GET', 'POST'])
def emailverificationforsignup():
    if request.method == 'POST':
        return redirect(url_for('login'))
    
    return render_template("emailforsignup.html")

@app.route('/submit-job', methods=['POST'])
def submit_job():
    company_name = request.form['company-name']
    job_role = request.form['job-role']
    experience_years = request.form['experience-years']
    experience_months = request.form['experience-months']
    salary = request.form['salary']
    mode = request.form['mode']
    technology_stack = request.form['technology-stack']
    comp_loc = request.form['comp-loc']
    job_description = request.form['job-description']
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert data into the table
    insert_query = '''
        INSERT INTO job_posts (company_name, job_role, experience_years, experience_months, salary, mode, technology_stack, company_location, job_description)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_query, (company_name, job_role, experience_years, experience_months, salary, mode, technology_stack, comp_loc, job_description))

    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('employerdashboard'))

# 2 means employer

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/employerabout')
def employerabout():
    return render_template('employerabout.html')

@app.route('/searchresults')
def searchresults():
   return render_template('searchresults.html')

@app.route('/searchresultsb',methods=['GET'])
def searchresultsb():
   return redirect(url_for('searchresults'))

@app.route('/employerdashboard',methods=['GET'])
def employerdashboard():
   return render_template('employerdb.html')

@app.route('/employerpostjob',methods=['GET'])
def employerpostjob():
   return render_template('postjob.html')

@app.route('/employerjobposted',methods=['GET'])
def employerjobposted():
   return render_template('jobsposted.html')

@app.route('/employerreports',methods=['GET'])
def employerreports():
   return render_template('reports.html')

@app.route('/employershortlisted',methods=['GET'])
def employershortlisted():
   return render_template('shortlisted.html')

@app.route('/employeedashboard',methods=['GET'])
def employeedashboard():
   return render_template('employeedb.html')

@app.route('/employeefindjobs',methods=['GET'])
def employeefindjobs():
   return render_template('findjobs.html')

@app.route('/employeejobsapplied',methods=['GET'])
def employeejobsapplied():
   return render_template('jobsapplied.html')

@app.route('/employeejobsstatus',methods=['GET'])
def employeejobsstatus():
   return render_template('jobsstatus.html')

@app.route('/employeeprofile',methods=['GET'])
def employeeprofile():
   return render_template('profile.html')

@app.route('/employeecontactus',methods=['GET'])
def employeecontactus():
   return render_template('employeecontactus.html')

@app.route('/jobcard1',methods=['GET'])
def employeejobcard1():
   return render_template('jobcard1.html')

@app.route('/jobcard2',methods=['GET'])
def employeejobcard2():
   return render_template('jobcard2.html')

@app.route('/jobcard3',methods=['GET'])
def employeejobcard3():
   return render_template('jobcard3.html')

@app.route('/jobcard4',methods=['GET'])
def employeejobcard4():
   return render_template('jobcard4.html')

@app.route('/jobcard5',methods=['GET'])
def employeejobcard5():
   return render_template('jobcard5.html')

@app.route('/updateprofile', methods=['GET'])
def updateprofile():
    return render_template('updateprofile.html')

if __name__ == '__main__':
    app.run(debug=True)

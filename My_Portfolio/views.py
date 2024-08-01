from datetime import datetime
from flask import render_template, request, flash, redirect, url_for, Blueprint,send_file
from My_Portfolio import app, db, mail
from flask_mail import Message
import os

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    completion_time = db.Column(db.String(50), nullable=False)
    github_link = db.Column(db.String(200), nullable=False)
    is_hosted = db.Column(db.String(3), nullable=False, default=False)

    
class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home Page', year=datetime.now().year)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        new_contact = Contact(name=name, email=email, subject=subject, message=message)
        db.session.add(new_contact)
        db.session.commit()

        msg = Message(subject=subject, recipients=['samarthvohra2003@gmail.com'])
        msg.body = f"From: {name} <{email}>\n\n{message}"
        
        try:
            mail.send(msg)
            flash('Message sent successfully!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            flash(f'Failed to send message. {str(e)}', 'danger')
    
    return render_template('contact.html')



@app.route('/about')
def about():
    # Path to the folder containing JPG files
    certification_folder = os.path.join(app.static_folder, 'certifications')

    # List all JPG files in the folder
    certificates = [file for file in os.listdir(certification_folder) if file.lower().endswith('.jpg')]

  
    skills = Skill.query.all()

    return render_template('about.html', skills=skills, certificates=certificates)


@app.route('/projects')
def projects():
    all_projects = Project.query.all()
    if all_projects:
        for project in all_projects:
            print(f"Project: {project.title}, Description: {project.description}")  # Debugging log
    else:
        print("No projects found")
    return render_template('projects.html', projects=all_projects)

@app.route('/hireme')
def hireme():
    return render_template('hireme.html')
@app.route('/view_cv')
def view_cv():
    return send_file('static/CV.pdf', as_attachment=False)

@app.route('/download_cv')
def download_cv():
    return send_file('static/CV.pdf', as_attachment=True)
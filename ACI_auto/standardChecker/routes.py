from flask import Blueprint,render_template,flash, request
from ACI_auto.standardChecker.forms import StandardCheckerForm
from ACI_auto import app
from flask_login import login_required
import os
import subprocess
from werkzeug.utils import secure_filename
import uuid
import shutil
import json
from ACI_auto.users.utils import allowed_file

standardChecker = Blueprint('standardChecker',__name__)

@standardChecker.route("/standard_checker_iss", methods=['GET', 'POST'])
@login_required
def standard_checker_iss():
    form = StandardCheckerForm()
    if form.validate_on_submit():
        unique_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(uuid.uuid4()))
        os.makedirs(unique_folder, exist_ok= True)

        files = request.files.getlist('files')
        error_message = None
        saved_files = []
        if not files or files == [None]:
            error_message = f"No files selected for processing!"
        else:
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(unique_folder, filename)
                    file.save(file_path)
                    saved_files.append(file_path)
                else:
                    if file.filename:
                        error_message = f"File {file.filename} has an invalid extension!"
                    else:
                        error_message = "No files selected!"
                    break

        if error_message:
            flash(error_message, 'danger')
            shutil.rmtree(unique_folder)
            return render_template('standard_checker.html',title='Standard Checker-ISS',form=form, stream = 'ISS')
        else:
            try:
                result = subprocess.run(['python','ACI_auto/scripts/codeStandardChecker.py','ISS',form.pr.data] + saved_files , capture_output=True, text=True)
                if result.returncode == 0:
                    res=json.loads(result.stdout)
                    validation_results = res["results"]
                    total_comments = res["count"]
                    return render_template('result.html',title='result',validation_results=validation_results, total_comments=total_comments) 
                else:
                    flash('Error!', 'danger')
                    flash(result.stderr, 'danger')
                    return render_template('result.html',title='result')
            except Exception as e:
                flash('Error in running the script!')
        shutil.rmtree(unique_folder)
        return render_template('result.html',title='result')        
    return render_template('standard_checker.html',title='Standard Checker-ISS',form=form, stream = 'ISS')

@standardChecker.route("/standard_checker_acq", methods=['GET', 'POST'])
@login_required
def standard_checker_acq():
    form = StandardCheckerForm()
    if form.validate_on_submit():
        unique_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(uuid.uuid4()))
        os.makedirs(unique_folder, exist_ok= True)

        files = request.files.getlist('files')
        error_message = None
        saved_files = []
        if not files or files == [None]:
            error_message = f"No files selected for processing!"
        else:
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(unique_folder, filename)
                    file.save(file_path)
                    saved_files.append(file_path)
                else:
                    if file.filename:
                        error_message = f"File {file.filename} has an invalid extension!"
                    else:
                        error_message = "No files selected!"
                    break
                 
        if error_message:
            flash(error_message, 'danger')
            shutil.rmtree(unique_folder)
            return render_template('standard_checker.html',title='Standard Checker-ACQ',form=form, stream = 'ACQ')
        else:
            try:
                result = subprocess.run(['python','ACI_auto/scripts/codeStandardChecker.py','ACQ',form.pr.data] + saved_files , capture_output=True, text=True)
                if result.returncode == 0:
                    res=json.loads(result.stdout)
                    validation_results = res["results"]
                    total_comments = res["count"]
                    return render_template('result.html',title='result',validation_results=validation_results, total_comments=total_comments) 
                else:
                    flash('Error!', 'danger')
                    flash(result.stderr, 'danger')
                    return render_template('result.html',title='result')
            except Exception as e:
                print(e)
                flash('Error in running the script!')
        shutil.rmtree(unique_folder)
               
    return render_template('standard_checker.html',title='Standard Checker-ACQ',form=form, stream = 'ACQ')

@standardChecker.route("/standard_checker_icg", methods=['GET', 'POST'])
@login_required
def standard_checker_icg():
    form = StandardCheckerForm()
    if form.validate_on_submit():
        unique_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(uuid.uuid4()))
        os.makedirs(unique_folder, exist_ok= True)

        files = request.files.getlist('files')
        error_message = None
        saved_files = []
        if not files or files == [None]:
            error_message = f"No files selected for processing!"
        else:
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(unique_folder, filename)
                    file.save(file_path)
                    saved_files.append(file_path)
                else:
                    if file.filename:
                        error_message = f"File {file.filename} has an invalid extension!"
                    else:
                        error_message = "No files selected!"
                    break
                 
        if error_message:
            flash(error_message, 'danger')
            shutil.rmtree(unique_folder)
            return render_template('standard_checker.html',title='Standard Checker-ICG',form=form, stream = 'ICG')
        else:
            try:
                result = subprocess.run(['python','ACI_auto/scripts/codeStandardChecker.py','ICG',form.pr.data] + saved_files , capture_output=True, text=True)
                if result.returncode == 0:
                    res=json.loads(result.stdout)
                    validation_results = res["results"]
                    total_comments = res["count"]
                    return render_template('result.html',title='result',validation_results=validation_results, total_comments=total_comments) 
                else:
                    flash('Error!', 'danger')
                    flash(result.stderr, 'danger')
                    return render_template('result.html',title='result')
            except Exception as e:
                flash('Error in running the script!')
        shutil.rmtree(unique_folder)
        return render_template('result.html',title='result')        
    return render_template('standard_checker.html',title='Standard Checker-ICG',form=form, stream = 'ICG')

from app import app
from flask import render_template, request, flash, redirect, url_for
from app.db import get_docs, post_doc, delete_doc
from app.score import calculate_score

import datetime

@app.route('/')
def index():      
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    all_docs = get_docs()
    all_stores = []
    for id in all_docs:
        all_stores.append(id['doc'])
    return render_template('dashboard.html', all_stores = all_stores)

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        document = {
            "name" : request.form['name'],
            "category": request.form['category'],
            "environmental_commitment" : request.form['environmental_commitment'],
            "operations" : 
                {
                    "delivery": request.form['delivery'],
                    "pickup": request.form['pickup']
                }
            ,
            "calculated_eco_score": calculate_score(request.form),
            "insert_datetime": str(datetime.datetime.now()),
            "update_datetime": str(datetime.datetime.now())
        }

        post_doc(document)
 
        flash("Created new record successfully")
 
        return redirect(url_for('results'))


@app.route('/update', methods = ['POST'])
def update():
    if request.method == 'POST':
        document = {
            "_id" : request.form['id'],
            "_rev": request.form['rev'],
            "name": request.form['name'],
            "category": request.form['category'],
            "environmental_commitment": request.form['environmental_commitment'],
            "operations": {
                "delivery": request.form['delivery'],
                "pickup": request.form['pickup']
            },
            "calculated_eco_score": calculate_score(request.form),
            "insert_datetime": str(datetime.datetime.now()),
            "update_datetime": str(datetime.datetime.now())
        }

        post_doc(document)
 
        flash("Updated record successfully")
 
        return redirect(url_for('dashboard'))


@app.route('/delete')
def delete():
    selected_document_id = request.values['_id']

    flash('Deleted: ' + selected_document_id)

    delete_doc(selected_document_id)
    return redirect(url_for('dashboard'))
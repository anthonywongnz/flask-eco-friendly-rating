from app import app
from flask import render_template, request, flash, redirect, url_for
from app.db import get_docs, post_doc, delete_doc

# shift this to db logic?
import datetime
import json

@app.route('/')
def index():


    all_docs = get_docs()

    all_stores = []


    for id in all_docs:
        all_stores.append(id['doc'])

    return render_template('index.html', all_stores = all_stores)


@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
        document = {
            "name" : request.form['name'],
            "category": request.form['category'],
            "packaging" : request.form['packaging'],
            "city": request.form['city'],
            "insert_datetime": str(datetime.datetime.now())
        }

        print('document received')
        print(document)

        # document = {
        #     "name" : "this is a test",
        #     "category":"test",
        #     "packaging" : "hello",
        #     "city": "Hamilton",
        #     "insert_datetime": str(datetime.datetime.now())
        #     }

        post_doc(document)
 
        flash("Created new record successfully")
 
        return redirect(url_for('index'))



@app.route('/delete')
def delete():
    selected_document_id = request.values['_id']
    # selected_document = json.loads(selected_document)
    flash('Deleting: ' + selected_document_id)

    delete_doc(selected_document_id)
    return redirect(url_for('index'))
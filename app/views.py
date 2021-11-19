from app import app
from flask import render_template, request, flash, redirect, url_for
from app.db import get_docs, post_doc, delete_doc
from app.score import calculate_score

import datetime
import ast

@app.route('/')
def index():      
    return render_template('index.html')

@app.route('/browse')
def browse():
    all_docs = get_docs()
    all_stores = []
    for id in all_docs:
        store = id['doc']
        store['calculated_eco_score'] = calculate_score(store)
        all_stores.append(store)

    return render_template('browse.html', all_stores = all_stores)

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

@app.route('/add-rating', methods = ['POST'])
def add_rating():
    if request.method == 'POST':

        delivery = request.form.get('delivery', 'n')
        if delivery == 'delivery':
            delivery = 'y'

        pickup = request.form.get('pickup', 'n')
        if pickup == 'pickup':
            pickup = 'y'

        dine_in = request.form.get('dine_in', 'n')
        if dine_in == 'dinein':
            dine_in = 'y'

        vegetarian_vegan = request.form.get('vegetarian_vegan', 'n')
        if delivery == 'vegetarian_vegan':
            delivery = 'y'

        plant_based_meat = request.form.get('plant_based_meat', 'n')
        if pickup == 'plant_based_meat':
            pickup = 'y'

        meat = request.form.get('meat', 'n')
        if dine_in == 'meat':
            dine_in = 'y'

        family_friendly = request.form.get('family_friendly', 'n')
        if delivery == 'family_friendly':
            delivery = 'y'

        pet_friendly = request.form.get('pet_friendly', 'n')
        if pickup == 'pet_friendly':
            pickup = 'y'

        previous_consumer_ratings = request.form.get('prev_consumer_ratings', '{}')

        if previous_consumer_ratings != '{}': # inserted first time
            previous_consumer_ratings = request.form['prev_consumer_ratings'][1:-1]
        else:
            previous_consumer_ratings = ''

        
        previous_consumer_ratings = ast.literal_eval(previous_consumer_ratings)

        document = {
            "_id" : request.form['id'],
            "_rev": request.form['rev'],
            "name" : request.form['name'],
            "category": request.form['category'],
            "environmental_commitment" : request.form['environmental_commitment'],
            "operations" : 
                {
                    "delivery": delivery,
                    "pickup": pickup,
                    "dine_in": dine_in,
                    "dispose_practices": request.form['dispose_practices'],
                    "electricity": request.form['electricity'],
                    "water": request.form['water'],
                    "website_link": request.form['website_link']
                },
            "consumer_ratings": [ 
                {
                    "family_friendly": family_friendly,
                    "pet_friendly": pet_friendly,
                    "vegetarian_vegan": vegetarian_vegan,
                    "plant_based_meat": plant_based_meat,
                    "meat": meat,
                    "food_source": request.form['food_source'],
                    "takeaway_packaging": request.form['takeaway_packaging'],
                    "takeaway_cutlery": request.form['takeaway_cutlery']
                }
            ],
            "calculated_eco_score": 0,
            "insert_datetime": str(datetime.datetime.now()),
            "update_datetime": str(datetime.datetime.now())
        }

        # if previous document has multiple ratings
        if (type(previous_consumer_ratings) is tuple):
            for i in previous_consumer_ratings:
                document['consumer_ratings'].append(i)
        else:
            document['consumer_ratings'].append(previous_consumer_ratings)

        post_doc(document)
 
        flash("Rating added successfully")
 
        return redirect(url_for('browse'))

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':

        # TO DO: FIX CHECKBOX
        delivery = request.form.get('delivery', 'n')
        if delivery == 'delivery':
            delivery = 'y'

        pickup = request.form.get('pickup', 'n')
        if pickup == 'pickup':
            pickup = 'y'

        dine_in = request.form.get('dine_in', 'n')
        if dine_in == 'dinein':
            dine_in = 'y'

        document = {
            "name" : request.form['name'],
            "category": request.form['category'],
            "environmental_commitment" : request.form['environmental_commitment'],
            "operations" : 
                {
                    "delivery": delivery,
                    "pickup": pickup,
                    "dine_in": dine_in,
                    "dispose_practices": request.form['dispose_practices'],
                    "electricity": request.form['electricity'],
                    "water": request.form['water'],
                    "website_link": request.form['website']
                },
            "consumer_ratings": {},
            "calculated_eco_score": 0,
            "insert_datetime": str(datetime.datetime.now()),
            "update_datetime": str(datetime.datetime.now())
        }

        post_doc(document)
 
        flash("Created new record successfully")
 
        return redirect(url_for('dashboard'))


@app.route('/update', methods = ['POST'])
def update():
    if request.method == 'POST':

        delivery = request.form.get('delivery', 'n')
        if delivery == 'delivery':
            delivery = 'y'

        pickup = request.form.get('pickup', 'n')
        if pickup == 'pickup':
            pickup = 'y'

        dine_in = request.form.get('dine_in', 'n')
        if dine_in == 'dinein':
            dine_in = 'y'

        document = {
            "_id" : request.form['id'],
            "_rev": request.form['rev'],
            "name": request.form['name'],
            "category": request.form['category'],
            "environmental_commitment": request.form['environmental_commitment'],
            "operations": {
                "delivery": delivery,
                "pickup": pickup,
                "dine_in": dine_in,
                "dispose_practices": request.form['dispose_practices'],
                "electricity": request.form['electricity'],
                "water": request.form['water'],
                "website_link": request.form['website']
            },
            "calculated_eco_score": 0,
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
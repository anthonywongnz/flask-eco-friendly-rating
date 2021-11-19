def calculate_score(store):

    scoring_matrix = {
        "food_options": {
            "weight": 8,
            "vegetarian_vegan": 1,
            "plant_based_meat": 1,
            "meat": 0
        },
        "takeaway_packaging": {
            "weight": 3,
            "compostable": 2,
            "plastic": -1,
            "biodegradable": 1,
            "na": 0
        },
        "takeaway_cutlery": {
            "weight": 2,
            "compostable": 2,
            "plastic": -1,
            "biodegradable": 1,
            "na": 0
        },
        "food_source": {
            "weight": 7,
            "local": 1,
            "not_local": -1
        },
        "dispose_practices": {
            "weight": 6,
            "recycle": 1,
            "landfill": -1,
            "compost": 2
        },
        "electricity": {
            "weight": 5,
            "renewable": 2,
            "hybrid": 2,
            "none": -1
        },
        "water": {
            "weight": 4,
            "most": 2,
            "some": 1,
            "none": -1
        }
    }

    total_score = 0

    # Score for disposing waste
    if store['operations']['dispose_practices'] == 'recycle':
        total_score += scoring_matrix['dispose_practices']['weight'] * \
            scoring_matrix['dispose_practices']['recycle']
    elif store['operations']['dispose_practices'] == 'landfill':
        total_score += scoring_matrix['dispose_practices']['weight'] * \
            scoring_matrix['dispose_practices']['landfill']
    elif store['operations']['dispose_practices'] == 'compost':
        total_score += scoring_matrix['dispose_practices']['weight'] * \
            scoring_matrix['dispose_practices']['compost']


    # Score for electricity
    if store['operations']['electricity'] == 'renewable':
        total_score += scoring_matrix['electricity']['weight'] * \
            scoring_matrix['electricity']['renewable']
    elif store['operations']['electricity'] == 'hybrid':
        total_score += scoring_matrix['electricity']['weight'] * \
            scoring_matrix['electricity']['hybrid']
    elif store['operations']['electricity'] == 'none':
        total_score += scoring_matrix['electricity']['weight'] * \
            scoring_matrix['electricity']['none']


    # Score for water
    if store['operations']['water'] == 'most':
        total_score + scoring_matrix['water']['weight'] * \
            scoring_matrix['water']['most']
    elif store['operations']['water'] == 'some':
        total_score += scoring_matrix['water']['weight'] * \
            scoring_matrix['water']['some']
    elif store['operations']['water'] == 'none':
        total_score += scoring_matrix['water']['weight'] * \
            scoring_matrix['water']['none']

    vote_count = len(store['consumer_ratings'])

    for rating in store['consumer_ratings']:

        # Score for food options
        if rating['vegetarian_vegan'] == 'y':
            total_score + scoring_matrix['food_options']['weight'] * \
                scoring_matrix['food_options']['vegetarian_vegan']
    
        if rating['plant_based_meat'] == 'y':
                total_score += scoring_matrix['food_options']['weight'] * \
                    scoring_matrix['food_options']['plant_based_meat']

        if rating['meat'] == 'y':
                total_score += scoring_matrix['food_options']['weight'] * \
                    scoring_matrix['food_options']['meat']
    
        # Score for food source
        if rating['food_source'] == 'local':
            total_score + scoring_matrix['food_source']['weight'] * \
                scoring_matrix['food_source']['local']
        elif rating['food_source'] == 'not_local':
            total_score + scoring_matrix['food_source']['weight'] * \
                scoring_matrix['food_source']['not_local']


        # Score for takeaway packaging
        if rating['takeaway_packaging'] == 'na':
            total_score + scoring_matrix['food_source']['weight'] * \
                scoring_matrix['takeaway_packaging']['na']
        elif rating['takeaway_packaging'] == 'compostable':
            total_score + scoring_matrix['takeaway_packaging']['weight'] * \
                scoring_matrix['takeaway_packaging']['compostable']
        elif rating['takeaway_packaging'] == 'plastic':
            total_score + scoring_matrix['takeaway_packaging']['weight'] * \
                scoring_matrix['takeaway_packaging']['plastic']
        elif rating['takeaway_packaging'] == 'biodegradable':
            total_score + scoring_matrix['takeaway_packaging']['weight'] * \
                scoring_matrix['takeaway_packaging']['biodegradable']


        # Score for takeaway cutlery
        if rating['takeaway_cutlery'] == 'na':
            total_score + scoring_matrix['food_source']['weight'] * \
                scoring_matrix['takeaway_cutlery']['na']
        elif rating['takeaway_cutlery'] == 'compostable':
            total_score + scoring_matrix['takeaway_cutlery']['weight'] * \
                scoring_matrix['takeaway_cutlery']['compostable']
        elif rating['takeaway_cutlery'] == 'plastic':
            total_score + scoring_matrix['takeaway_cutlery']['weight'] * \
                scoring_matrix['takeaway_cutlery']['plastic']
        elif rating['takeaway_cutlery'] == 'biodegradable':
            total_score + scoring_matrix['takeaway_cutlery']['weight'] * \
                scoring_matrix['takeaway_cutlery']['biodegradable']
    
    if vote_count == 0:
        average_score = 0
    else:
        average_score = round(total_score / vote_count, 2)
    return average_score

def get_vote_count(store):
    return len(store['consumer_ratings'])

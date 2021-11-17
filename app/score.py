def calculate_score(store):

    scoring_matrix = {
        "food_options": {
            "weight": 8,
            "vegetarian_vegan": 1,
            "plant_based_meat": 1,
            "meat": 0
        },
        "packaging": {
            "weight": 3,
            "compostable": 2,
            "plastic": -1,
            "biodegradable": 1,
            "reusable cup discounts": 2,
            "no plastic bags": 2,
        },
        "cutlery_takeaway": {
            "weight": 2,
            "compostable": 2,
            "plastic": -1,
            "biodegradable": 1,
            "reusable cup discounts": 2,
            "no plastic straws": 2,
        },
        "cutlery_in_store": {
            "weight": 2,
            "compostable": 2,
            "plastic": -1,
            "biodegradable": 1,
            "reusable cup discounts": 2,
            "no plastic straws": 2,
        },
        "food_source_scores": {
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
    if store.get('dispose_practices') == 'recycle':
        total_score += scoring_matrix['dispose_practices']['weight'] * \
            scoring_matrix['dispose_practices']['recycle']
    elif store.get('dispose_practices') == 'landfill':
        total_score += scoring_matrix['dispose_practices']['weight'] * \
            scoring_matrix['dispose_practices']['landfill']
    elif store.get('dispose_practices') == 'compost':
        total_score += scoring_matrix['dispose_practices']['weight'] * \
            scoring_matrix['dispose_practices']['compost']


    # Score for electricity
    if store.get('electricity') == 'renewable':
        total_score += scoring_matrix['electricity']['weight'] * \
            scoring_matrix['electricity']['renewable']
    elif store.get('electricity') == 'hybrid':
        total_score += scoring_matrix['electricity']['weight'] * \
            scoring_matrix['electricity']['hybrid']
    elif store.get('electricity') == 'none':
        total_score += scoring_matrix['electricity']['weight'] * \
            scoring_matrix['electricity']['none']


    # Score for water
    if store.get('water') == 'most':
        total_score += scoring_matrix['water']['weight'] * \
            scoring_matrix['water']['most']
    elif store.get('water') == 'some':
        total_score += scoring_matrix['water']['weight'] * \
            scoring_matrix['water']['some']
    elif store.get('water') == 'none':
        total_score += scoring_matrix['water']['weight'] * \
            scoring_matrix['water']['none']

    return total_score
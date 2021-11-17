def calculate_score(store):
    print('score calc')
    print(store)
    total_score = 0
    if store['delivery'] == 'y':
        total_score = 10
    else:
        total_score = 0
    return total_score
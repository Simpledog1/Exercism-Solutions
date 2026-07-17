import math
def score(x, y):
    formula = x**2 + y**2
    distance = math.sqrt(formula)

    score = 0
    if distance <= 1:
        score = 10
    elif distance <= 5:
        score = 5
    elif distance <= 10:
        score = 1
    else:
        score = 0
    return score
    

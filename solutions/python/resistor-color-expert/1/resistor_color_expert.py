def resistor_label(colors):
    color = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    tolerance = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%"
    }
    if len(colors) == 1:
        return f"{color[colors[0]]} ohms" 
        
    elif len(colors) == 4:
        first = color[colors[0]]
        second = color[colors[1]]
        multiplier = color[colors[2]]
        base = first * 10 + second
        result = base * (10**multiplier)
        tol = tolerance[colors[3]]
        
    elif len(colors) == 5:
        first = color[colors[0]]
        second = color[colors[1]]
        third = color[colors[2]]
        multiplier = color[colors[3]]
        base = (first * 10 + second) * 10 + third 
        result = base * (10**multiplier)
        tol = tolerance[colors[4]]
        
    unit = ""
    if result >= 1_000_000_000:
        result /= 1_000_000_000
        unit = "gigaohms"
    elif result >= 1_000_000:
        result /= 1_000_000
        unit = "megaohms"
    elif result >= 1_000:
        result /= 1_000
        unit = "kiloohms"
    else:
        if result == 1:
            unit = "ohm"
        else:
            unit = "ohms"
    
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    return f"{result} {unit} ±{tol}"
        
        

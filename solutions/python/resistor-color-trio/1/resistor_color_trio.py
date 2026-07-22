def label(colors):
    color = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]
    first = color.index(colors[0])
    second = color.index(colors[1])
    third = color.index(colors[2])
    base = first * 10 + second
    result = base * (10**(third))
    
    if result >= 1000000000:
        final_result = result // 1000000000
        return f"{final_result} gigaohms"
    elif result >= 1000000:
        final_result = result // 1000000
        return f"{final_result} megaohms"
    elif result >= 1000 and result % 1000 == 0:
        final_result = result // 1000
        return f"{final_result} kiloohms"
    elif result == 1:
        return f"{final_result} kiloohm"
    return f"{result} ohms"
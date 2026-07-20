def value(colors):
    color = [ "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    first = color.index(colors[0])
    second = color.index(colors[1])
    result = first * 10 + second
    return result
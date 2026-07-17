def line_up(name, number):
    final_number = str(number)
    if str(number).endswith(("11","12","13")):
        final_number = str(number) + "th"
    elif str(number).endswith("1"):
        final_number = str(number) + "st"
    elif str(number).endswith("2"):
        final_number = str(number) + "nd"
    elif str(number).endswith("3"):
        final_number = str(number) + "rd"
    else:
        final_number = str(number) + "th"
    return (f"{name}, you are the {final_number} customer we serve today. Thank you!")
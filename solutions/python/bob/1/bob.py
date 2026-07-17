def response(hey_bob):
    bob = hey_bob.strip()  
    if not bob:
        return "Fine. Be that way!"
    has_letter = False
    for i in hey_bob:
        if i.isalpha():
            has_letter = True
    if has_letter and hey_bob.isupper() and bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if has_letter and hey_bob.isupper():
        return "Whoa, chill out!"
    if bob.endswith("?"):
        return "Sure."   
    else:
        return "Whatever."
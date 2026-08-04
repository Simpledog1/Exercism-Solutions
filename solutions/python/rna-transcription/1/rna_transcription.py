def to_rna(dna_strand):
    result = ""
    for i in dna_strand:
        if i == "C":
            result += "G"
        elif i == "G":
            result += "C"
        elif i == "T":
            result += "A"
        elif i == "A":
            result += "U"
    return result

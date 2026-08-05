def append(list1, list2):
    return list1 + list2

def concat(lists):
    result = []
    for sublist in lists:
        for item in sublist:
            result += [item]
    return result
    
    
def filter(function, list):
    result = []
    for i in list:
        if function(i):
            result += [i]
    return result

def length(list):
    return len(list)

def map(function, list):
    result = []
    for lists in list:
        result += [function(lists)]
    return result
            
def foldl(function, list, initial):
    result = initial
    for lists in list:
        result = function(result,lists)
    return result

def foldr(function, list, initial):
    result = initial
    for lists in reversed(list):
        result = function(result, lists)
    return result

def reverse(list):
    result = []
    for i in reversed(list):
        result += [i]
    return result
        

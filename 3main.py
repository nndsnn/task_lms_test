class MessageMatchError(Exception):
    pass

class EmptyResultError(Exception):
    pass

def witch_signs(*tuples):
    result = []
    
    for string, substring in tuples:
        if len(substring) > len(string):
            raise ValueError("Too long substring")
        
        if substring == string:
            raise MessageMatchError("There should not be an exact match")
        
        if string.startswith(substring) or string.endswith(substring):
            result.append(string)
    
    if not result:
        raise EmptyResultError("There is nothing to return")
    
    return result
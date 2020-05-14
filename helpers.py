

def valid_boolean_input(user_input):
    try:
        x = user_input.lower().strip()
    except ValueError:
        pass
    if x in ["true", "yes", "y"]: 
        return True
    if x in ["false", "no", "n"]: 
        return False
    else: 
        return "error"
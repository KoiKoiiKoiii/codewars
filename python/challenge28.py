def string_to_number(s):
    try:
        return int(s)
    except (ValueError):
        return "Input is not valid " 

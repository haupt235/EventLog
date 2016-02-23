def mean(numbs):
    
    try:
        num_vals = len(numbs)
    except TypeError:
        return numbs

    try:
        ret_val = float(sum(numbs))/len(numbs)
    except ZeroDivisionError:
        return None


    return ret_val


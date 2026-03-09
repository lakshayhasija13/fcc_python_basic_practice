def number_pattern(n):
    string = ""
    if isinstance(n, int):
        if n <= 0:
            return 'Argument must be an integer greater than 0.'
        else:
            for i in range(1, n+1):
                string += str(i) + " "
            return string[:-1]
    else:
        return 'Argument must be an integer value.'

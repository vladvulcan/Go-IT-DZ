def solve_riddle(riddle, word_length, start_letter, reverse=False):    
    if start_letter in riddle:
        if not reverse:
            start = riddle.index(start_letter)
            end = start+word_length
            word = riddle[start:end]
        else:
            reverse_riddle = riddle[::-1]
            start = reverse_riddle.index(start_letter)
            end = start+word_length
            word = reverse_riddle[start:end]
    else: word = ''
    return word
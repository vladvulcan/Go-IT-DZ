def sequence_buttons(string):
    numbers = [i for i in range(1,10)]
    buttons = ['0']
    for num in numbers:
        num = str(num)    
        if num == '1':
            l = 5        
        elif num in '79':
            l = 4
        else:
            l = 3
        for cnt in range(1,l+1):
                buttons.append(num*cnt) 
    letters = ' .,?!:ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    let_to_but = {}
    for let, but in zip(letters, buttons):
        let_to_but[ord(let)] = but
    for let, but in zip(letters[6:], buttons[6:]):
        let_to_but[ord(let.lower())] = but

    res = string.translate(let_to_but)
    return res
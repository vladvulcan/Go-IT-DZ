def decode(code, res =0):
    if res == 0:
        res = []
    if len(code) != 0:
        chr = code[0]
        cnt = code[1]
        for i in range(1,cnt+1):
            res.append(chr)
        if len(code) > 2:
            return decode(code[2:], res)

    return res
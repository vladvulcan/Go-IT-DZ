def encode(data, res = 0):
    if res == 0:
        res = []
    if len(data) >0:
        chr = data[0]
        cnt = 1
        for i in data[1:]:
            if i in 'XYZ':
                if i == chr:
                    cnt += 1
                else:
                    res.append(chr)
                    res.append(cnt)
                    return encode (data[data.index(i):], res)
        res.append(chr)
        res.append(cnt)

    return res
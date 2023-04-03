def all_sub_lists(data):
    output = [[]]
    size = len(data)
    if size != 0:
        for i in range(size):
            output.append([data[i]])
        for i in range(len(data)):
            if data[i] != data[-1]:            
                output.append([data[i],data[i+1]])

        if size > 3:
            out = []
            for i in range(size-1):
                out.append(data[i])
            output.append(out)
            out = [] 
            for i in range(1,size):
                out.append(data[i])
            output.append(out)
        
        output.append(data)
    return output
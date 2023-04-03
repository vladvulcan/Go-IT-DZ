def to_indexed(source_file, output_file):
    output = []
    with open (source_file,'r') as file1:
        text = file1.readlines()        
        for line, num in zip (text, range(len(text))):
            out = f'{num}: {line}'
            output.append(out)
    with open (output_file,'w') as file2:
        file2.writelines(output)
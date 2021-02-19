def list_of_problems_preprocess():
    """
    docstring
    """
    with open('0_list_of_problems', 'r') as f:
        lines = f.readlines()
    lines = [line.replace('\t', '. ') for line in lines]

    with open('0_list_of_problems', 'w') as f:
        for i in range(0,len(lines), 2):
            f.write(lines[i])

def create_files():
    """ """
    with open("0_list_of_problems", 'r') as f:
        lines = f.readlines()
    print(lines)
    for i in range(len(lines)):
        for a in range(len(lines[i])):
            if lines[i][a] == ' ':
                lines[i] = lines[i][a+1:]
                break
        for a in range(len(lines[i])):
            if lines[i][a] == ".":
                lines[i] = lines[i][:a-1]
                break
    
    print(lines)

create_files()
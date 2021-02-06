
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

def create_files_by_given_list():
    """
    docstring
    """
    pass
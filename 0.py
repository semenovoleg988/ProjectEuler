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
    for i in range(len(lines)):
        for a in range(len(lines[i])):
            if lines[i][a] == ' ':
                lines[i] = lines[i][a+1:]
                break
        for a in range(len(lines[i])):
            if lines[i][a] == ".":
                lines[i] = lines[i][:a]
                break
    for i in range(29, len(lines)):
        with open(str(i+1) + ".py", 'w') as f:
            f.write("# Problem " + str(i+1) + '\n' + "# " + lines[i])
        lines[i] = lines[i].replace(" ", "_").lower()
        with open(str(i+1) + ".py", 'a') as f:
            f.write("\n# Description(https://projecteuler.net/problem=" + str(i+1)+ ")\n")
            f.write("\n\ndef " + lines[i] + "() -> None:\n")
            f.write("    \"\"\" \"\"\"\n")
            f.write("    pass\n")
            f.write("\n\nif __name__ == \"__main__\":\n")
            f.write("    pass")

create_files()
def read_input_file_generate_integer_list():
    with open("C:/Users/PrinceLuhanga/Desktop/Personal/Advent of Code 2023/Advent-of-Code-2023/Day 1/Day1_Input.txt",
              "r") as file:
        contents = file.read()
        lines = contents.splitlines()
        array_of_lines_without_alphas = []
        for line in lines:
            temp_list = []
            for char in line:
                if char.isnumeric():
                    temp_list.append(int(char))
            array_of_lines_without_alphas.append(temp_list)

    return array_of_lines_without_alphas



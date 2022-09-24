
with open('anime.json') as file:
    read_file = file.readlines()
    # print(read_file)
    for names in read_file:
        print(names)
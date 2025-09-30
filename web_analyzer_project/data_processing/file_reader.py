def read_data(file_path):
    data = []
    with open(file_path, "r") as file:
        for line in file:
            name, age = line.strip().split(",")
            data.append((name, int(age)))
    return data

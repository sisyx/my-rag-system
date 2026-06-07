def load_data() -> str:
    with open("data/sample.txt", "r") as file:
        contents = file.read()
        return contents

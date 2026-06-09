def load_document(path: str) -> str:
    with open(path, "r") as file:
        contents = file.read()
        return contents

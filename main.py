import chuncker
import loader

if __name__ == "__main__":
    data = loader.load_data()
    chunks = chuncker.chunk_text(data, 100, 10)
    for chunk in chunks:
        print(chunk)

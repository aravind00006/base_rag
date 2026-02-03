import os


def load_documents(data_dir: str):
    """
    Load .txt files from a directory and return a list of documents.
    Each document is represented as a dict with:
    - text: file content
    - source: filename
    """
    documents = []

    if not os.path.isdir(data_dir):
        raise ValueError(f"Provided path is not a directory: {data_dir}")

    for filename in os.listdir(data_dir):
        if not filename.endswith(".txt"):
            continue

        file_path = os.path.join(data_dir, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read().strip()

                if not text:
                    continue

                documents.append({
                    "text": text,
                    "source": filename
                })

        except Exception as e:
            # Fail gracefully: skip bad files
            print(f"Skipping file {filename}: {e}")

    return documents


if __name__ == "__main__":
    docs = load_documents("./data")

    print(f"Total documents loaded: {len(docs)}\n")

    for doc in docs:
        print(f"Source: {doc['source']}")
        print(doc["text"][:200])
        print("-" * 40)

from loader import load_documents

def chunk_documents(documents, chunk_size=600):  
    """Split documents into fixed-size character chunks."""

    chunks = []

    for doc in documents:
        text = doc["text"]
        source = doc["source"]

        start = 0
        chunk_id = 0

        while start < len(text):
            chunk_text = text[start:start + chunk_size]

            chunks.append({
                "chunk_start": start,
                "text": chunk_text,
                "source": source,
                "chunk_id": chunk_id
            })

            start += chunk_size
            chunk_id += 1

    return chunks


if __name__ == "__main__":

    documents = load_documents("./data")
    chunks = chunk_documents(documents, chunk_size=600)

    print(f"Total documents input: {len(documents)}")
    print(f"Total chunks output: {len(chunks)}")

    if documents:
        first_doc_source = documents[0]["source"]
        doc_chunks = [c for c in chunks if c["source"] == first_doc_source]

        print(f"\nChunks for document: {first_doc_source}")
        print(f"Number of chunks: {len(doc_chunks)}")

        if doc_chunks:
            print("\nFirst chunk preview:")
            print(doc_chunks[0]["text"][:200])

            print("\nLast chunk preview:")
            print(doc_chunks[-1]["text"][:200])

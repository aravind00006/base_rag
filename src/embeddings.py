from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def embed_chunks(chunks):
    """Input= chunks ----> output= embeddings, metadata"""

    texts = []
    for chunk in chunks:
        texts.append(chunk["text"])

    response = client.embeddings.create(
        model='text-embedding-3-small',
        input = texts
    )

    embeddings = []
    for item in response.data:
        embeddings.append(item.embedding)

    metadata = [
        {
            'source': chunk['source'],
            "chunk_id": chunk['chunk_id']
        }
        for chunk in chunks
    ]
    return embeddings, metadata

if __name__ == "__main__":
    from loader import load_documents
    from chunker import chunk_documents
    print("embeddings.py started")
    documents = load_documents("./data")
    chunks = chunk_documents(documents, chunk_size=600)

    embeddings, metadata = embed_chunks(chunks)
    print(f"Number of chunks embedded: {len(embeddings)}")
    print(f"Embedding vector dimension: {len(embeddings[0])}")
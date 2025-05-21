from langchain_ollama import OllamaEmbeddings

def get_embeddings():
    embedding_model = None
    try:
        embedding_model = OllamaEmbeddings(model="mxbai-embed-large:335m")
    except Exception:
        print("Failed to create OLLama Embeddings model")
    return embedding_model

def get_retriever(vector_store):
    return vector_store.as_retriever(
    search_type="mmr", search_kwargs={"k": 5, "fetch_k": 5}
)
from langchain_chroma import Chroma

def vector_store_fetch(embedding_model):
    return Chroma(
        collection_name="gitlab_collection",
        embedding_function=embedding_model,
        persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
    )

def vector_store_retriever(vector_store):
    return vector_store.as_retriever(
        search_type="mmr", search_kwargs={"k": 5, "fetch_k": 5}
    )
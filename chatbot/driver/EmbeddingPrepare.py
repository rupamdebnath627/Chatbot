from langchain_community.document_loaders import RecursiveUrlLoader
from langchain_text_splitters import HTMLSemanticPreservingSplitter
from embeddings.EmbeddingUtil import get_embeddings
from vectorstore.VectorStoreUtil import vector_store_fetch

if __name__ == "__main__":
    loader = RecursiveUrlLoader(
        "https://handbook.gitlab.com/",
        base_url="https://handbook.gitlab.com/",
        prevent_outside=True
    )

    docs = loader.lazy_load()

    headers_to_split_on = [
        ("h1", "Header 1"),
        ("h2", "Header 2"),
    ]

    splitter = HTMLSemanticPreservingSplitter(
        headers_to_split_on=headers_to_split_on,
        separators=["\n\n", "\n", ". ", "! ", "? "],
        max_chunk_size=50,
        preserve_images=False,
        preserve_videos=False,
        elements_to_preserve=["table", "ul", "ol"],
        denylist_tags=["script", "style", "head"]
    )

    documents = splitter.transform_documents(docs)

    embedding_model = get_embeddings()
    vstore = vector_store_fetch(embedding_model)

    max_batch_size = 50

    def batch_documents(batch_docs, batch_size):
        for i in range(0, len(batch_docs), batch_size):
            yield batch_docs[i:i+batch_size]

    for batch in batch_documents(documents, max_batch_size):
        vstore.add_documents(documents=batch)
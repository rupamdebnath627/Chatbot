from embeddings.EmbeddingUtil import get_embeddings
from vectorstore.VectorStoreUtil import vector_store_fetch, vector_store_retriever
from chatbot.gradio.GradioLauncher import launch_gradio
from dotenv import load_dotenv, find_dotenv

if __name__ == "__main__":
    load_dotenv(find_dotenv())

    embedding_model = get_embeddings()
    vstore = vector_store_fetch(embedding_model)
    retriever = vector_store_retriever(vstore)
    launch_gradio(retriever)


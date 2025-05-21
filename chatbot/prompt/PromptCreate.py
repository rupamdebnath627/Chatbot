from langchain_core.prompts import PromptTemplate

def create_prompt(retrieved_docs,question):
    prompt = PromptTemplate(
    template="""
        You are a helpful assistant.
        Answer ONLY from the provided context.
        If the context is insufficient, just say you don't know.
        Please summarize answer under 100 words.
        
        {context}
        Question: {question}
        """,
        input_variables = ['context', 'question']
    )

    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

    return prompt.invoke({"context": context_text, "question": question})
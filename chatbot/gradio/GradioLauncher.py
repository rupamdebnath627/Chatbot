import gradio as gr
from langchain_core.messages import HumanMessage, AIMessage
from chatbot.llmmodel.LLMModerCreator import fetch_llm_model
from chatbot.prompt.PromptCreate import create_prompt

def launch_gradio(retriever):
    history_langchain_format = []

    def stream_response(message, history):
        model = fetch_llm_model()
        for msg in history:
            if msg['role'] == "user":
                history_langchain_format.append(HumanMessage(content=msg['content']))
            elif msg['role'] == "assistant":
                history_langchain_format.append(AIMessage(content=msg['content']))
        history_langchain_format.append(
            HumanMessage(content=create_prompt(retriever.invoke(message),message).to_string())
        )
        gpt_response = model.invoke(history_langchain_format)
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": gpt_response.content})
        return "", history


    def clear_chat():
        history_langchain_format.clear()
        return "", []

    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(type="messages")
        textbox = gr.Textbox(placeholder="Send to the LLM...",
                             type="text",
                             container=False,
                             autoscroll=True,
                             scale=10)
        submit_btn = gr.Button("Submit")
        clear_btn = gr.Button("Clear Chat")

        submit_btn.click(fn=stream_response, inputs=[textbox, chatbot], outputs=[textbox, chatbot])
        clear_btn.click(fn=clear_chat, outputs=[textbox, chatbot])

    demo.launch()
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import gradio as gr

model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def chat(user_input, history=[]):
    # Prepare input for DialoGPT format
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    # Concatenate with history if available
    bot_input_ids = torch.cat([torch.tensor(history).squeeze(0), new_input_ids], dim=-1) if history else new_input_ids

    # Generate response
    output_ids = model.generate(
        bot_input_ids,
        max_length=bot_input_ids.shape[1] + 100,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )

    # Decode response
    response = tokenizer.decode(output_ids[:, bot_input_ids.shape[1]:][0], skip_special_tokens=True)

    # Update history
    history = output_ids

    return response, history.tolist()

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🤖 Smart Chatbot with DialoGPT")
    chatbot_output = gr.Textbox(label="Chatbot", interactive=False)
    user_input = gr.Textbox(label="You", placeholder="Ask me anything!")

    state = gr.State([])

    def respond(user_text, history):
        response, history = chat(user_text, history)
        return response, history

    user_input.submit(respond, [user_input, state], [chatbot_output, state])

demo.launch()
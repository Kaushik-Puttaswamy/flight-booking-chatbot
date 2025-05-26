from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import gradio as gr

# Load pre-trained model and tokenizer
model_name = "distilgpt2"  # Smaller than GPT2
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Chat function
def chat(user_input, history=[]):
    # Append user input to history
    history.append(user_input)
    # Format conversation history
    prompt = " ".join(history)
    
    # Encode input and generate response
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    response_ids = model.generate(
        input_ids,
        max_length=input_ids.shape[1] + 50,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.9
    )
    
    # Decode response and update history
    response = tokenizer.decode(response_ids[:, input_ids.shape[1]:][0], skip_special_tokens=True)
    history.append(response)
    return response, history

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## 🤖 Simple AI Chatbot")
    chatbot_output = gr.Textbox(label="Chatbot", interactive=False)
    user_input = gr.Textbox(label="You", placeholder="Type something and press Enter")

    state = gr.State([])

    def respond(user_text, history):
        response, history = chat(user_text, history)
        return response, history

    user_input.submit(respond, [user_input, state], [chatbot_output, state])

# Run the chatbot UI
demo.launch()
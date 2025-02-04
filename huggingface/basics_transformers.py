# Load model directly

# Imports
import os
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Access a secret stored as an environment variable
HF_TOKEN=os.environ['HF_TOKEN']


model_name = "meta-llama/Llama-3.2-1B"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

# Custom model storage directory
model_path = "./huggingface/models"
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=model_path)
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=model_path)


# Set device to CPU or GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)


# Generate text 
def generate_text(prompt, max_tokens=100):
    inputs = tokenizer(user_input, return_tensors="pt").to(device)
    output = model.generate(**inputs, max_new_tokens=max_tokens)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Providing input
user_input = "Hello, how are you?"
response = generate_text(user_input)
print(response)

# Fix `attention_mask` and `pad_token_id` were not set by setting pad_token_id:
# def generate_text(prompt, max_tokens=100):
#   inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
#   inputs = {k: v.to(device) for k, v in inputs.items()}
#   output = model.generate(**inputs, pad_token_id=tokenizer.pad_token_id, max_new_tokens=max_tokens)

# user_input = "Hello, how are you?"
# response = generate_text(user_input)
# print(response)



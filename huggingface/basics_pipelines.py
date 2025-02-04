import os
from transformers import pipeline

# Access a secret stored as an environment variable
HF_TOKEN=os.environ['HF_TOKEN']

# Text generation example
generator = pipeline("text-generation", model="meta-llama/Llama-3.2-1B",use_auth_token=HF_TOKEN)
result = generator("Write a haiku about recursion in programming.", max_length=100)

print(result)

# Text summarization example
# summarizer = pipeline("summarization", model="meta-llama/Llama-3.2-1B", use_auth_token=HF_TOKEN)
# text = "Hugging Face is an amazing library that provides various models for tasks such as natural language processing..."
# summary = summarizer(text, max_length=100, min_length=50)

# print(summary)

# Text Translation example

# translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr", use_auth_token=HF_TOKEN)
# text = "How are you doing today?"
# translation = translator(text)
# print(translation)
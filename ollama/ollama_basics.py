import os
import ollama

image_path = r"C:\Data\aiplayground\ollama\image.jpg"

response = ollama.chat(
    model='llama3.2-vision:11b',
    messages=[{
        'role': 'user',
        'content': 'What is in this image?',
        'images': [image_path]  # Use the absolute path
    }]
)


print(response)
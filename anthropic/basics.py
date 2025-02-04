import os
import anthropic

# Access OpenAI API secrets stored as environment variables
# anthropic_api_key = os.environ['ANTHROPIC_API_KEY']



client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.environ['ANTHROPIC_API_KEY'],
)

message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=8192,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Why is the ocean salty?"
                }
            ]
        }
    ]
)
print(message.content)
import os
from openai import OpenAI

# Access OpenAI API secrets stored as environment variables
openai_api_key = os.environ['OPENAI_API_KEY']
openai_api_org_id = os.environ['OPENAI_ORG_ID']
openai_deployment_id = os.environ['OPENAI_PROJECT_ID']

client = OpenAI(api_key=openai_api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
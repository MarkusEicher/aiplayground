import os
import cohere 

co = cohere.Client(
  api_key=os.environ['COHERE_API_KEY'], # This is your trial API key
) 

stream = co.chat_stream( 
  model='command',
  message='<YOUR MESSAGE HERE>',
  temperature=0.3,
  chat_history=[],
  prompt_truncation='AUTO',
  # connectors={connectors}
) 

for event in stream:
  if event.event_type == "text-generation":
    print(event.text, end='')
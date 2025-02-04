import os
from ai21 import AI21Client
from ai21.models.chat import ChatMessage, ResponseFormat, DocumentSchema, FunctionToolDefinition, ToolDefinition, ToolParameters, UserMessage

message = UserMessage(content="Why is the ocane salty?") 

client = AI21Client(api_key=os.environ.get("AI21_API_KEY"))
response =client.chat.completions.create(
		model="jamba-1.5-mini",
		messages=[message],
		documents=[],
		tools=[],
		n=1,
		max_tokens=2048,
		temperature=0.4,
		top_p=1,
		stop=[],
		response_format=ResponseFormat(type="text"),
)

print(response)
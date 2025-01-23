
# Chat Function with ChatGPT

import openai

chat_log = []

while True:
	user_message = input()
	if user_message.lower() =="quit":
		break
	else:
		chat_log.append({"role": "user", "content": user_message})
		response = openai.ChatCompletion.create(
	model = "gpt-version",
	messages = chat_log
	)
	assistant_response = response.choices[0]messages.content
	print("ChatGPT:", assistant_response.strip())
	chat_log.append({"role": "assistant", "content": assistant_response.strip()})
	print(response.usage.total_tokens)
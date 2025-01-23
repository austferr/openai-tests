
# Chat Function with ChatGPT

import os                                                            # import environment variables.
from openai import OpenAI                                            # import OpenAI library.

client = OpenAI()                                                    # set new alias.

client.api_key = os.environ.get("OPENAI_API_KEY")                    # pulls env var OPENAI_API_KEY.

chat_log = []                                                        # dictionary of prompts/responses.

while True:
	user_message = input()                                           # request input.
	if user_message.lower() =="quit":                                # if input='quit': break
		break                                                        
	else:
		chat_log.append({"role": "user", "content": user_message})   # valid input, append to chat_log.
		response = client.ChatCompletion.create(                     # defines output as response.
	model = "gpt-version",                                           # model version.
	messages = chat_log                                              # user messages are referenced as the chat log.
	)
	assistant_response = response.choices[0].messages.content        # specifies response content.
	print("ChatGPT:", assistant_response.strip())                    # print model response.
	chat_log.append({"role": "assistant", "content": assistant_response.strip()})   # append cleaned response to chat_log.

print(response.usage.total_tokens)                                   # print amount of tokens used.


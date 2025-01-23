> ## Resources
> **Videos**
> [Use OpenAI's ChatGPT in Python](https://www.youtube.com/watch?v=YVFWBJ1WVF8)
> [AI and Python - OpenAI API with Python Introduction](https://www.youtube.com/watch?v=I6T9Ztn0S-M)
> **OpenAI**
> [Quickstart](https://platform.openai.com/docs/quickstart)
> [Pricing](https://openai.com/api/pricing/)
> **Prompt Engineering**
> [Prompt Engineering Guide](https://www.promptingguide.ai/)
> [Jupyter Notebooks](https://www.promptingguide.ai/notebooks)
> [Prompting Techniques](https://www.promptingguide.ai/techniques)
> [Risks & Misuses](https://www.promptingguide.ai/risks)
## API
**Generate Keys**
> [OpenAI Developer Platform](https://platform.openai.com)
##### Prompt Schema
each individual request is generated with the context information.
costs *# of* **tokens**.
```Python
import openai
API_KEY = open("file_name", "r").read()
openai.api_key = API_KEY

response = openai.ChatCompletion.create(
	model="gpt-version",
	messages=[{"role": "user", "content": "What is the difference between Python and C++?"}, ...]

print(response)
```
##### Roles
**USER** the user requesting
**ASSISTANT** GPT itself
**SYSTEM** context information
```Python
response = openai.ChatCompletion.create(
	model="gpt-version",
	messages=[
	{"role": "system", "content": "You are a a helpful assistant that writes Python scripts?"},
	{"role": "user", "content": "What script can I use to create a working clock?"}]
```
### Chat System
appends chat log with responses.
```Python
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
	assistant_response = response.choices[0]message.content
	print("ChatGPT:", assistant_response.strip())
	chat_log.append({"role": "assistant", "content": assistant_response.strip()})
	print(response.usage.total_tokens)
```
### DALL E
GPT creates a URL to host the image.
using **get** allows for downloading the image automatically.
```Python
from openai import OpenAI
from requests import get

client = OpenAI()

query = 'a cat in the ocean'

response = client.images.generate(
	model="dall-e-3",
	prompt=query,
	n=1, # how many images to return.
	size="1024x1024" # medium sizes,
)
print(response)
print("***")
print(response.created)
print("***")
print(response.data[0].revised_prompt)
print("***")
print(response.data[0].url)

pic_name = f'{response.created}.png'

response_image = get(response.data[0].url)

with open(pic_name, 'wb') as file:
	file.write(response_image.content) # saves to User folder.
```

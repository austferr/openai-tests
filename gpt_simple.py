
import os                                                 # import environment variables.
from openai import OpenAI                                 # import OpenAI library.

client = OpenAI()                                         # set new alias.

client.api_key = os.environ.get("OPENAI_API_KEY")         # pulls env var OPENAI_API_KEY.

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "system", "content": "You are a a helpful assistant that writes can explain weather phenomenon?"},           # prompt example.
	{"role": "user", "content": "What is the difference between a tornado and a twister?"}],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_completion_tokens=5,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)                                           # print response.
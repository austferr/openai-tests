
import os                                                 # import environment variables.
from openai import OpenAI                                 # import OpenAI library.

client = OpenAI()                                         # set new alias.

client.api_key = os.environ.get("OPENAI_API_KEY")         # pulls env var OPENAI_API_KEY.

response = client.ChatCompletion.create(                  # defines response as output
	model="gpt-version",                                  # model version
	messages=[
	{"role": "system", "content": "You are a a helpful assistant that writes Python scripts?"},           # prompt example.
	{"role": "user", "content": "What script can I use to create a working clock?"}]                      # prompt example.
)

print(response)                                           # print response in full.
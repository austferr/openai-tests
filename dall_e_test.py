
import os                                                 # import environment variables.
from openai import OpenAI                                 # import OpenAI library.

client = OpenAI()                                         # set new alias.

client.api_key = os.environ.get("OPENAI_API_KEY")         # pulls env var OPENAI_API_KEY.

query = 'a cat in the ocean'                              # prompt.

response = client.images.generate(                        # define output as response.
	model="dall-e-3",                                     # model type.
	prompt=query,                                         # input.
	n=1,                                                  # how many images to return.
	size="1024x1024"                                      # sizes: 1024x1024, 1792x1024, 1024x1792
)
print(response)                                           # prints response in full.
print("***")
print(response.created)                                   # timestamp.
print("***")
print(response.data[0].revised_prompt)                    # GPT revises the input prompt to generate image.
print("***")
print(response.data[0].url)                               # URL where file is hosted.

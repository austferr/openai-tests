
from openai import OpenAI           # need check imports

client = OpenAI()

query = 'a cat in the ocean'               # prompt for generation of image.

response = client.images.generate(
	model="dall-e-3",
	prompt=query,
	n=1,                                   # how many images to return.
	size="1024x1024"                       # sizes: 
)
print(response)
print("***")
print(response.created)
print("***")
print(response.data[0].revised_prompt)     # GPT revises the input prompt to generate image.
print("***")
print(response.data[0].url)                # URL where file is hosted.


from openai import OpenAI                  # need check imports
from requests import get                   # adds get from requests

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

pic_name = f'{response.created}.png'       # names file.

response_image = get(response.data[0].url)

with open(pic_name, 'wb') as file:
	file.write(response_image.content)     # saves to User folder.
# openai_tests
for practicing, testing, openai prompts

-----

## !
an **API key** will need to be generated and added in order to run scripts.

in PowerShell use:

```
setx OPENAI_API_KEY "key"
```

sets a local environment variable that is called using:

```
import os
from openai import OpenAI

client = OpenAI()
client.api_key = os.environ.get("OPENAI_API_KEY")
```

-----

## gpt_simple.py
*basic formatting test for sending requests to chatGPT model.*

directly returns response.

## gpt_chat_log.py
*creates a chat log of user and assistant responses.*

directly returns response contents until given **quit**.

## dall_e_test.py
*basic test for sending request to Dall-E model to generate an image.*

directly returns response and statistics. URL for image viewing and download.

## py_info.md
*general notes for syntax, prompt engineering, etc.*

-----

### Updates
- fixed VScode not **import**ing openai. // *changed to **Python 3.13.1***
- updated MD Syntax in README and GPT with Python. // *for viewing purposes*
- removed **get** function for background testing. // *used to download image auto*
- added way of using ENV VAR **OPENAI_API_KEY**. // *to allow for users to set locally, avoid using a file*

-----

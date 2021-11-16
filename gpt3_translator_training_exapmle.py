
from gpt import GPT, Example   #import gpt.py script
import openai

openai.api_key = 'YOUR-KEY'

# Translator Use-case
gpt = GPT(engine="davinci", temperature=0.5, max_tokens=100)
# Examples to train as a English to French translator
gpt.add_example(Example('What is your name?', 'quel est votre nom?'))
gpt.add_example(Example('What are you doing?', 'Que faites-vous?'))
gpt.add_example(Example('How are you?', 'Comment allez-vous?'))

# Input to the model
prompt = "where are you?"
output = gpt.submit_request(prompt)
# Model output
print(output.choices[0].text)
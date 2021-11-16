import openai

def gpt3(stext):
    openai.api_key = 'YOUR-KEY'  
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=stext,
        temperature=0.1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0].text)

query="What is Dark Matter?"
gpt3(query)


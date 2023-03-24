import sys
import openai
import os

prompt = sys.argv[1]

openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key != None:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print(completion.choices[0].message.content)
else:
    print("No API key detected, please add your valid OpenAI APi key or press Ctrl/Cmd+C to exit\nYou can add the API key as an environment variable 'OPENAI_API_KEY'")
    apiKey = input("Add Key here: ") 
    os.system("setx OPENAI_API_KEY " + apiKey)

# print("No Api key detected, PLease add a valid openAI key.")

# 


# print(completion.choices[0].message)

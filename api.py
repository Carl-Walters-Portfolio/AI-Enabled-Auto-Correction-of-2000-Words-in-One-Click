import os
import openai




class Api():
    def call(self, aiText, userText):
        openai.api_key = 'Please create an open AI account and create an API key'
        text=aiText + " " + userText
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0,
        max_tokens=2000,
        top_p=0.2,
        frequency_penalty=0,
        presence_penalty=0
        )

        print(response["choices"][0]["text"])
        
        return response["choices"][0]["text"]

import os
import openai




class Api():
    def call(self, _text):
        openai.api_key = 'please create an openai account and setup an api key to place here'
        text="Correct the spelling of the following text? " + _text
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        print(response["choices"][0]["text"])
        
        return response["choices"][0]["text"]

import os
import openai


class Api():
    """
    Controls openai API Further functions will be built into this to give greater control over parameters
    """
    def call(self, aiText, userText):
        """
        Combine's AI prompt and user text and calls the open API with this

        Args:
            aiText (Str): text from the Ai prompt in the GUI this text should be at the beginning because the GUI encourages the user to use this part as the prompt
            userText (Str): Users text from the GUI from the section which is for text that may be for manipulation which is handled by theaiText 

        Returns:
            _type_: _description_
        """
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
        
        return response["choices"][0]["text"]

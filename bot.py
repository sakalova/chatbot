import openai
import os
from dotenv import load_dotenv


load_dotenv()


class ChatBot:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.organization = os.getenv("OPENAI_ORGANIZATION_KEY")
        openai.Model.list()

    def get_api_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=500,
            temperature=0.7  # the less this value the more accurate is response, the more - the response more diverse
        ).choices[0].text
        return response

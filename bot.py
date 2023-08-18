"""
Help on module bot:

NAME
    bot - This module provides a class for interacting with OpenAI's GPT API.

The module contains the following class:
- `ChatBot()` - This class is used to make requests and receive responses to/from OpenAI's GPT API.
"""

import os

import openai
from dotenv import load_dotenv

load_dotenv()


class ChatBot:
    """This class is used to make requests and receive responses to/from OpenAI's GPT API."""
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.organization = os.getenv("OPENAI_ORGANIZATION_KEY")
        openai.Model.list()

    @staticmethod
    def get_api_response(user_input: str) -> str:
        """
        Calling OpenAI's GPT API to provide text output to user input.

        Chat models take an input and return a model-generated message as output.

        Args:
         user_input: A string text that represents user input

        Returns:
            A string text that represents OpenAI's response on user input with the maximum number
            of tokens to generate in the completion that equals the value of `max_tokens`.
        """
        response = (
            openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=500,
                temperature=0.7,  # the less this value the more accurate response is
            )
            .choices[0]
            .text
        )
        return response

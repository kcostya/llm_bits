""" Utility functions for the project. """
from typing import List

import openai


def get_completion(
    prompt: str, model: str = "gpt-3.5-turbo", temperature: float = 0.0
) -> str:
    """
    Get completion for the given prompt using OpenAI model and chat completion endpoint:
    https://platform.openai.com/docs/guides/chat.

    :param prompt: The user prompt for generating completion.
    :param model: The model name to use for completion. Default is "gpt-3.5-turbo".
    :param temperature: The temperature value to control the randomness of the completion. Default is 0.
    :return: The generated completion text as a string.
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


def get_completion_from_messages(
    messages: List[str], model: str = "gpt-3.5-turbo", temperature: float = 0.0
) -> str:
    """Perform completion of a conversation using OpenAI Chat models.

    :param messages: A list of messages in the conversation.
    :param model: The name of the chat model to use. Default is "gpt-3.5-turbo".
    :param temperature: The temperature for randomness of the model's output. Default is 0.0.
    :return: The completed response as a string.
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

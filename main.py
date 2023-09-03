from textbase import bot
from textbase.models import OpenAI
from typing import List
from textbase.configEnv import settings

# Import your custom Message class here
from textbase.message import Message
# Set the OpenAI API key
OpenAI.api_key = settings.KEY

# Initialize conversation history
conversation_history = []

@bot()
def on_message(message_history: List[Message], state: dict = None):
    # Extract user messages from the conversation history and check for the role
    user_messages = [message['content'] for message in message_history if message['role'] == 'user']
    user_messages_text = ' '.join([message[0]['value'] for message in user_messages])

    # Determine the chatbot's role based on the user's input
   # Determine the chatbot's role based on the user's input
   # Determine the chatbot's role based on the user's input
# Determine the chatbot's role based on the user's input
    if "movie" in user_messages_text.lower():
        personalized_prompt = "You are a chatbot created by Jhanvi to provide recommendations to users. " \
                            "Whether you're interested in discovering great movies or exploring captivating books, " \
                            "I'm here to help! Feel free to ask for movie suggestions or book recommendations, " \
                            "and I'll do my best to assist you. Let's dive into the world of entertainment and literature together!\n"
    else:
        personalized_prompt = "You are a chatbot created by Jhanvi to provide recommendations to users. " \
                            "Whether you're looking for movie recommendations or seeking out interesting books, " \
                            "I've got you covered! Feel free to ask about movies or books, and I'll provide suggestions " \
                            "based on your preferences. Let's embark on a journey of discovery through movies and literature!\n"



    # Include the user's latest message in the prompt for context
    if user_messages:
        personalized_prompt += f"User: {user_messages[-1]}\n"

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=personalized_prompt,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }

import openai
import config

openai.api_key = config.api_key

# Context of the assistent
messages = [{"role": "system", "content": "Eres un asistente muy util"}]

while True:

    content = input("Escribe tu pregunta (si quieres terminar el chat escribe: salir): ")

    if content == "salir":
        break

    messages.append({"role": "user", "content": content})

    # Try spanish question to openai chat-gpt-api beta ref: https://platform.openai.com/docs/api-reference/chat/create 
    response = openai.ChatCompletion.create(model = "gpt-3.5-turbo", temperature = 0.7, max_tokens = 500, top_p = 1, frequency_penalty = 0, presence_penalty = 0.6,
                                messages = messages)
    
    # pass the response of the conversation to the role assistant
    messages.append({"role": "assistant", "content": response.choices[0].message.content})


    print(response.choices[0].message.content)
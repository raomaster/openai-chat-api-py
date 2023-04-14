import openai
import config
import typer
from rich import print
from rich.table import Table

def main():
    openai.api_key = config.api_key

    print("💬 [bold green]Welcome to the OpenAI Chatbot![/bold green]")

    # Create a table with commands
    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    # Context of the assistent
    context = [{"role": "system", "content": "Eres un asistente muy útil"}]

    messages = context

    while True:

        content = __prompt()

        if content == "mew":
            print("💬 [bold green]Nueva conversación creada[/bold green]")
            messages = context
            content = __prompt()

        messages.append({"role": "user", "content": content})

        # Try spanish question to openai chat-gpt-api beta ref: https://platform.openai.com/docs/api-reference/chat/create 
        response = openai.ChatCompletion.create(model = "gpt-3.5-turbo", temperature = 0.7, max_tokens = 500, top_p = 1, frequency_penalty = 0, presence_penalty = 0.6,
                                    messages = messages)
        
        # pass the response of the conversation to the role assistant
        messages.append({"role": "assistant", "content": response.choices[0].message.content})

        # print the response of the conversation to the console
        print(f"[bold green]> [/bold green] [green]{response.choices[0].message.content}[/green]")

def __prompt() -> str:
    prompt = typer.prompt("\nEscribe tu pregunta")
    # Check if the user wants to exit
    if prompt == "exit":
        # Confirm if the user wants to exit
        typer.confirm("❓ ¿Seguro que quieres terminar el chat?", default=False)
        raise typer.Abort()
    
    return prompt

if __name__ == "__main__":
    typer.run(main)
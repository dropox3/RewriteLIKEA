import openai
import tkinter as tk
from tkinter import simpledialog

openai.api_key = "YOUR API"


def construir_conversa(mensagens):
    conversa = ""
    for mensagem in mensagens:
        if mensagem["role"] == "system":
            conversa += f"{mensagem['content']}\n"
        else:
            conversa += f"{mensagem['role'].capitalize()}: {mensagem['content']}\n"
    return conversa

def get_completion(user_input):
    global mensagens
    mensagens.append({"role": "user", "content": user_input})
    
    entrada = construir_conversa(mensagens)
    
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=entrada,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    resposta_texto = completion.choices[0].text.strip()
    mensagens.append({"role": "assistant", "content": resposta_texto})
    
    return resposta_texto

def main():
    root = tk.Tk()
    root.withdraw()

    while True:
        user_input = simpledialog.askstring("Pergunta ou solicitação", "Digite sua pergunta ou solicitação: ") + " reescreva como essa pessoa " + simpledialog.askstring("Pessoa famosa", "Digite alguma pessoa famosa: ") + " escreveria"
        if user_input is None:
            break

        result = get_completion(user_input)
        simpledialog.messagebox.showinfo("Resposta", result)

if __name__ == "__main__":
    main()

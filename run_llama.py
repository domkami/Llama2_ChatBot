import os
model_path = "C:\\Users\\kamil\\OneDrive\\Desktop\\Projekty\\Python\\ChatBot\\llama\\llama-2-7b-chat.Q2_K.gguf"


print("Plik istnieje:", os.path.isfile(model_path))  # powinno być: True

from llama_cpp import Llama
llm = Llama(model_path=model_path)

def chat_with_llama(prompt):
    output = llm(prompt, max_tokens=100, stop=["\n"], echo=False)
    return output['choices'][0]['text'].strip()

if __name__ == "__main__":
    while True:
        user_input = input("Ty: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_llama(user_input)
        print("Llama2:", response)

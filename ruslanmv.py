import sys
import ollama
from langchain_community.llms import Ollama

def main():
    # Check if enough arguments are passed
    if len(sys.argv) < 2:
        print("Usage: python ruslanmv.py <your message>")
        return

    # Join the command line arguments to form the prompt
    prompt = " ".join(sys.argv[1:])
    
    # Replace with the desired model name
    model_name = "llama3:latest"
    
    # Check if you have the model
    models_info = ollama.list()
    models = [model['name'] for model in models_info['models']]
    
    if model_name not in models:
        print(f"Model {model_name} not found, downloading...")
        ollama.pull(model=model_name)
    else:
        print(f"Model {model_name} is already downloaded.")
    
    # Create the model
    llm = Ollama(model=model_name)
    
    # Generate a response
    response = llm.invoke(prompt)
    
    # Print the response
    print(response)

if __name__ == "__main__":
    main()

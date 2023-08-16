# Import necessary libraries
import tiktoken
from rich import print
from rich.prompt import Prompt
from tabulate import tabulate
from typing import Tuple
from rich.console import Console
import textwrap


console = Console()

# Existing functions from token2.py
def show_introduction():
    print("""
        This code demonstrates the tokenization process using the `tiktoken` library.
    """)

def num_tokens_from_string(string: str, model_name: str) -> int:
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(string))



def display_word_parameters(english_word: str, other_language_word: str, other_language_name: str, model_name: str):
    max_width = 50  # Adjust as needed
    
    # Word wrapping
    wrapped_english_word = textwrap.fill(english_word, max_width)
    wrapped_other_word = textwrap.fill(other_language_word, max_width)
    
    data = [
        ["Letters", ' '.join(wrapped_english_word), ' '.join(wrapped_other_word)],
        ["Character Count", str(len(english_word)), str(len(other_language_word))],
        #["Code Points", ' '.join([str(ord(c)) for c in english_word]), ' '.join([str(ord(c)) for c in other_language_word])],
        #["Bytes", ' '.join([str(b) for b in english_word.encode('utf-8')]), ' '.join([str(b) for b in other_language_word.encode('utf-8')])],
        ["Tokens", str(num_tokens_from_string(english_word, model_name)), str(num_tokens_from_string(other_language_word, model_name))]
    ]
    
    table_str = tabulate(data, headers=["Parameter", "English", other_language_name], tablefmt="fancy_grid")
    table_str = table_str.replace("Parameter", "[bold magenta]Parameter[/bold magenta]")
    table_str = table_str.replace("English", "[bold blue]English[/bold blue]")
    table_str = table_str.replace(other_language_name, f"[bold green]{other_language_name}[/bold green]")
    console = Console()
    console.print(table_str)


# Implementation based on the user's requirements
def get_custom_language_input() -> Tuple[str, str, str]:
    lang_code = input("Enter the ISO language code (e.g., en, en-EN, ENG): ")
    english_word = input("Enter a word or sentence in English: ")
    other_language_word = input(f"Enter the corresponding word or sentence in {lang_code}: ")
    return english_word, other_language_word, lang_code.upper()

def main():
    show_introduction()

    # Present user with the options
    choice = input("Choose an option:\n[a] Default (English and Bangla)\n[b] Custom\n") or "a"

    if choice.lower() == "a":
        english_word, other_language_word, other_language_name = "I speak Bengali", "আমি বাংলায় কথা কই", "Bangla"
    elif choice.lower() == "b":
        english_word, other_language_word, other_language_name = get_custom_language_input()
    else:
        print("[red]Invalid choice. Exiting.[/red]")
        return

    # Inform user about the model selection
    print("[bold green]Model is selected by default as gpt-3.5-turbo.[/bold green]")
    model_name = "gpt-3.5-turbo"
    
    # Display
    display_word_parameters(english_word, other_language_word, other_language_name, model_name)

main()




# GPTTokenCounter
A plain script to compare and count tokens for OpenAI 


### Introduction

OpenAIToken Counter is a simple Python script designed to provide insights into the tokenization process of various languages compared to English. 

### Dependencies

to run the script you need  the following Python libraries to be properly installed:

- `tiktoken`
- `rich`
- `tabulate`

To install these prerequisites, execute:

```bash
pip install tiktoken rich tabulate
```

### How to Execute OpenAIToken Counter

1. **Clone the Repository** 

2. **Execute the Script**:
    ```bash
    python GPTTokencounter.py
    ```
3. **Language Selection**:
    - The program kicks off with a brief overview of its purpose.
    - You'll then be prompted to either:
      - `[a] Default (English and Bangla)`
      - `[b] Custom`
  
      Choose the default for a comparison between English and Bangla, or opt for a custom language pair.

4. **Provide Required Inputs**:
    - For the custom option, you'll need to specify the ISO language code, an English word or sentence, and its counterpart in the chosen language.
  
5. **Examine the Token Comparison**:
    - The next step showcases a table contrasting the tokenization of the English phrase with the selected language, leveraging the `gpt-3.5-turbo` model.


### Useful Points

- The `tiktoken` library is the backbone, facilitating token count based on the model.
  
- The default model in use is `gpt-3.5-turbo`. Should you wish to experiment with others, adjust the `model_name` variable within the `main()` function.
  
- The `display_word_parameters()` function integrates word wrapping, ensuring legibility for lengthier inputs.

### Contributions and Feedback

We welcome feedback! If you come across any hiccups do reach out through GitHub.


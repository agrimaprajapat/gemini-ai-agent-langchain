from langchain.tools import tool

@tool
def calculator(expression: str) ->str:
    """Perform mathematical calculation."""
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"
    

@tool
def word_counter(text:str) ->str:
    """Count the number of words in the given text"""
    return f"Total words: {len(text.split())}"
                               
import openai
import argparse
from SetupLogger import setup_logging

# REFERENCE: For understanding the purpose and usage of OpenAI API: 
# https://beta.openai.com/docs/api-reference/introduction

class QUERYCOMPLETION:
    def __init__(self, API_KEY=None) -> str:
        """
        Constructor for QUERY class.
        
        This method initializes a QUERY instance and sets the OpenAI API key.
        
        Parameters:
        - API_KEY (str): The OpenAI API key. It's essential for making requests to OpenAI's GPT-3.5-turbo API.
        """
        
        self.API_KEY = API_KEY  # Assign provided API key to instance variable
        openai.api_key = self.API_KEY  # Set the API key for OpenAI API access

    def get_completion(self, prompt: str, model="gpt-3.5-turbo"):
        """
        Fetches and returns a model's completion for a given prompt using OpenAI API.
        
        Parameters:
        - prompt (str): The text input that will be expanded/completed by GPT-3.5-turbo.
        - model (str, optional): The model used for generating the completion. Defaults to "gpt-3.5-turbo".
        
        Returns:
        str: The generated completion from GPT-3.5-turbo.
        """
        
        # Constructing message payload for API request.
        # Role "user" indicates that the message content is a user's input to be processed by GPT-3.5-turbo.
        # OPTIMIZE: Consider implementing a method to detail queries in order to save on response message sizes and data rates.
        messages = [{"role": "user", "content": prompt}]

        # WARNING: GPT-3.5-turbo model completions may not always provide accurate or truthy information.
        # It is essential to treat the response as a suggestion rather than a definitive answer.
        # It might be valuable to add additional checks or validation for critical applications.
        
        # Sending API request to OpenAI and obtaining response.
        # Temperature is set to 0 to produce more deterministic output.
        response = openai.ChatCompletion.create(model=model, messages=messages, temperature=0)
        
        # Extracting and returning the model's message content from API response.
        return response.choices[0].message["content"]

if __name__ == "__main__":
    # Ensuring the script execution as main to avoid undesired code execution during import
    
    # Utilizing argparse to handle command-line argument parsing
    parser = argparse.ArgumentParser(description="Get API KEY and PROMPT as inputs and return GPT-3 completions for PROMPT.")
    
    # Defining a command-line argument for API key input
    parser.add_argument("API_KEY", type=str, help="Your OpenAI GPT-3 API Key.")
    parser.add_argument("PROMPT", type=str, help="Your AI Query Prompt.")
    
    # Parsing command-line arguments
    args = parser.parse_args()
    
    # Configuring logger for informational output
    logger = setup_logging()

    # Retrieving API key from parsed arguments
    api_key = args.API_KEY
    
    # Creating QUERY instance with provided API key
    query = QUERYCOMPLETION(api_key)

    # Retrieving the query prompt from parsed arguments
    prompt = args.PROMPT
    
    # Fetching and logging completion using get_completion method of QUERY instance
    completion = query.get_completion(prompt)
    
    logger.info("Prompt: %s", prompt)
    logger.info("Completion: %s", completion)

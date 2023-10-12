import openai
import pandas as pd
import json
import os
import boto3

class Query:
    def __init__(self, API_KEY=None, dynamoDB=None) -> None:
        self.API_KEY = API_KEY
        openai.api_key = self.API_KEY

    def get_completion(prompt:str, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(model=model,messages=messages,temperature=0,)
        return response.choices[0].message["content"]
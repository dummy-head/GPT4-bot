import openai
import pandas as pd
import numpy as np
import pickle
from transformers import GPT2TokenizerFast
from typing import List
import pyttsx3

openai.api_key = "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"
COMPLETIONS_MODEL = "text-davinci-003"



while(1):
	prompt = input("Q: ")

	result = openai.Completion.create(
	    prompt=prompt,
	    temperature=0,
	    max_tokens=300,
	    top_p=1,
	    frequency_penalty=0,
	    presence_penalty=0,
	    model=COMPLETIONS_MODEL,
	)["choices"][0]["text"].strip(" \n")

	print("~"*100)
	print(result)
	print("~"*100)
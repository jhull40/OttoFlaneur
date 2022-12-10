import pandas as pd
from gibberish import Gibberish
import random
import nltk
from nltk.corpus import wordnet
import os
import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_location():
    cities = pd.read_csv('data/worldcities.csv')[['city', 'country']]
    gib = Gibberish()

    if random.random() > 0.85:
        location = 0
        location = gib.generate_word()
    elif random.random() > 0.2:
        vals = random.choice(cities.values)
        location = f'{vals[0]}, {vals[1]}'
    else:
        location = random.choice(cities['city'])
    
    return location

def get_adjective(words):
    
    synonyms = []  
    for syn in wordnet.synsets(random.choice(words)):
        for l in syn.lemmas():
            synonyms.append(l.name())
            
    adjective = random.choice(synonyms)
    return adjective

def get_prompt(adjective, location):
    prompt = f'Create an instagram post about my recent {adjective} trip to {location}'
    return prompt

def get_gpt3_post(prompt):
    openai.api_key = OPENAI_API_KEY# os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
)
    return response['choices'][0]['text']


if __name__ == '__main__':
    some_words = ['excellent', 'amazing', 'great', 'boring', 'fun', 'interesting']
    location = get_location()
    adjective = get_adjective(some_words)
    prompt = get_prompt(adjective, location)
    post = get_gpt3_post(prompt)
    print(post)
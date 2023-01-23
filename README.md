# Otto Flaneur

This is a pseudo-serious, but mostly for banter project that leverages new AI models to create an instagram bot.

## Main Code
Many thanks to [simplemaps](https://simplemaps.com/data/world-cities) for providing a huge list (43,000) cities of the world. I randomly sample from this (but sometimes making up a fake word), to generate the location for my post. 

While I have a pre-defined set of a few words, I use [nltk](https://www.nltk.org/howto/wordnet.html) to generate some synonyms to change the words in the prompt. This prompt, which includes location and adjective selected at random, gets fed to GPT-3 to create an instagram post. That prompt then gets sent to stable diffusion to generate images for the post. 


## TODO
- Logging 
- venv/requirements updates
- holidays
- travel plan coordinator


### To test the project:
- Clone the repo.
- Create a `python virtual environment` using `venv` or `virtualenv`.
- run `pip install -r requirements.txt` to download required python libraries.
- The project uses `spaCy` for some tasks to install `spaCy` follow steps given [here](https://spacy.io/usage)
- After installing spacy run `python -m spacy download en_core_web_lg` to install the dataset for spaCy.
- `task1\Q1.ipynb` is the code when Restrictions are there all other code files are named properly.

# Task-1
## Aim: 
Implementing pseudo-unsupervised model to check Sentence similarity 
## Insights:
-  If we just convert words to vectors and then find the cosine similarity between them as an idea to find the similarity that would give false results.
    For example: if I just use tf\_idf vectors and apply cosine similarity then the result would be same for each sentence.
- Also in Word2Vec approach we see that for each word it uses words before and after that word to make context. **So if some words are randomly written and we train our model on that than we would find that the output given will be very wrong**.
- Also we observe that most of the python libraries like `spaCy`, `nltk` are not able to predict the similarity score if those words were not present in the training dataset. **nltk and spaCy doesn't use supervised learining but rather goes with pseudo-unsupervised/ unsupervised learing for predicting similarity**.

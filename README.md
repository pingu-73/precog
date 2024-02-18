### To test the project:
- Clone the repo.
- Create a `python virtual environment` using `venv` or `virtualenv`.
- run `pip install -r requirements.txt` to download required python libraries.
- The project uses `spaCy` for some tasks to install `spaCy` follow steps given [here](https://spacy.io/usage)
- After installing spacy run `python -m spacy download en_core_web_lg` to install the dataset for spaCy.
- `task1\Q1.ipynb` is the code when Restrictions are there all other code files are named properly.
- `precog-task-report` folder contains .tex and .bib codes along with figures for report.

# Task-1
## Aim: 
Implementing pseudo-unsupervised model to check Sentence similarity 
## Insights:
-  If we just convert words to vectors and then find the cosine similarity between them as an idea to find the similarity that would give false results.
    For example: if I just use tf\_idf vectors and apply cosine similarity then the result would be same for each sentence.
- Also in Word2Vec approach we see that for each word it uses words before and after that word to make context. **So if some words are randomly written and we train our model on that than we would find that the output given will be very wrong**.
- Also we observe that most of the python libraries like `spaCy`, `nltk` are not able to predict the similarity score if those words were not present in the training dataset. **nltk and spaCy doesn't use supervised learining but rather goes with pseudo-unsupervised/ unsupervised learing for predicting similarity**.

# Task-2
## Aim:
Given labeled data-set splitted into training, testing, dev. we have to predict the Phrase and sentence similarity.
## Approach:
- Altough the labelled data was given. But i've used unsupervided learning in this task.
- I'm using the frequency of how many pairs have similarity in the training data as my threshold frequency. And calculating if test pairs have similarity score $>$ threshold or not.
- Doing this would always give the similarity score to be 1. Because in the [dataset](https://huggingface.co/datasets/paws) each pair sentences are just paraphrased.
## Insights

- **for example:** consider these 2 sentences{\cite{paws2019naacl}} to follow the approch mentioned above.
    - In Paris , in October 1560 , he secretly met the English ambassador , Nicolas Throckmorton , asking him for a passport to return to `England through Scotland`.
    - In October 1560 , he secretly met with the English ambassador , Nicolas Throckmorton , in Paris , and asked him for a passport to return to `Scotland through England` .

- In the above example all the things are same except the highlighted part. As discussed in the **Task1** that for a given word word2vec looks at words before and after to make context of the words. Due to this reason the model can't tell the difference between the two sentences.
    
- Now consider this [example](https://huggingface.co/datasets/paws/viewer/labeled_final/test):
    - This was a series of nested `angular standards` , so that measurements in azimuth and elevation could be done directly in polar coordinates relative to the ecliptic .
    - This was a series of nested `polar scales` , so that measurements in azimuth and elevation could be performed directly in angular coordinates relative to the ecliptic .

- Over here the difference is pretty big but the model wan't able to identify the dissimilarity in these sentences. **So to tackle situations like this I also add a check to compare Parts of Speech for both Sentences**. 
    

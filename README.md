# ML NLP POS Lemmatization

Author: Zahra Dastfal  
Student Number: 700777425
Course: DSA 5600 — Machine Learning  
Assignment: Homework 4 — Part C (Coding)

---

## Description
This project contains Python code for performing basic NLP preprocessing steps on a sample sentence.  
It covers:
1. Tokenization  
2. Stopword removal  
3. Lemmatization (not stemming)  
4. Filtering only verbs and nouns using POS tags  

The code file: **ml_nlp_pos_lemmatization.py**

---

## Input Example
```text
"John enjoys playing football while Mary loves reading books in the library."

## Expected Output
Filtered lemmas (verbs & nouns only): ['John', 'enjoy', 'play', 'football', 'Mary', 'love', 'read', 'book', 'library']
As text: John enjoy play football Mary love read book library

## How to Run
1. **Install spaCy**
   ```bash
   pip install spacy
   python -m spacy download en_core_web_sm

2-Run the script
python ml_nlp_pos_lemmatization.py




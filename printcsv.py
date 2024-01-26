import pandas as pd
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz
import Levenshtein
import string
import numpy as np

TD = pd.read_csv("TestData.csv")
ED = pd.read_csv("ExistingBrands.csv")
word = []
for index,row in TD.iterrows():
    for col in ED.columns:
        if isinstance(row[col],str) and row[col] != "":
            wordlist = row[col].split()
            for i in range(len(wordlist)):
                for char in wordlist[i]:
                    if not char.isalpha():
                        newword=wordlist[i].replace(char, "", 1)
                        wordlist[i]=newword
                if wordlist[i] != "":
                    lowerword = wordlist[i].lower()
                    word.append(lowerword)
for index,row in ED.iterrows():
    for col in ED.columns:
        if isinstance(row[col],str) and row[col] != "":
            wordlist = row[col].split()
            for i in range(len(wordlist)):
                for char in wordlist[i]:
                    if not char.isalpha():
                        newword=wordlist[i].replace(char, "", 1)
                        wordlist[i]=newword
                if wordlist[i] != "":
                    lowerword = wordlist[i].lower()
                    word.append(lowerword)
with open("dataset.txt", "w") as file:
    for item in word:
        file.write(f"'{item}'\n")
token = [word]
model = Word2Vec(token, vector_size=300, window=5, min_count=1, sg=0)
model.save("mymodel.bin")


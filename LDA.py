#!/usr/bin/env python3
import os
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import nltk.stem.porter 
import numpy as np
import nltk
nltk.download('wordnet')
import pandas as pd
import pyLDAvis
import pyLDAvis.gensim
global directory
global stemmer
global result
result=[]
stemmer = SnowballStemmer("english")
directory = os.getcwd()

def files_10():
    #Change number to select file
    count=2
    data = pd.read_csv('file' + str(count) + '.csv')
    df = pd.DataFrame(data)
    print(df)
    for index, c in df.iterrows():
        lemmatize_stemming(c['"QUESTION' + str(count) + '"'])
        preprocess(lemma)
    print(result)
    text = 'Question ' + str(count)
    with open(text, "w") as result_file:
        result_file.write('')
    dictionary = gensim.corpora.Dictionary(result)
    bow_corpus = [dictionary.doc2bow(doc) for doc in result]
    bow_doc_x = bow_corpus[0]
    print(bow_doc_x)
    for i in range(len(bow_doc_x)):
        print("Word {} (\"{}\") appears {} time.".format(bow_doc_x[i][0], 
                                                         dictionary[bow_doc_x[i][0]], 
                                                         bow_doc_x[i][1]))
    lda_model =  gensim.models.LdaMulticore(bow_corpus, 
                       num_topics = 8, 
                       id2word = dictionary,                                    
                       passes = 10,
                       workers = 2)
    
    
    for idx, topic in lda_model.print_topics(-1):
        with open(text, "a") as result_file:
            result_file.write("Topic: {} \nWords: {}".format(idx, topic ) + "\n")
    vis = pyLDAvis.gensim.prepare(topic_model=lda_model, corpus=bow_corpus, dictionary=dictionary)
    pyLDAvis.enable_notebook()
    pyLDAvis.show(vis)
    
def lemmatize_stemming(i):
    global lemma
    lemma = stemmer.stem(WordNetLemmatizer().lemmatize(i, pos='v'))
    return lemma
# Tokenize and lemmatize
def preprocess(lemma):
    one = []
    for token in gensim.utils.simple_preprocess(lemma) :
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 2:
            one.append(lemmatize_stemming(token))   
    return result.append(one)

files_10()



#!/usr/bin/env python3
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import nltk.stem.porter 
import nltk
nltk.download('wordnet')
import pandas as pd
import pyLDAvis
import pyLDAvis.gensim
global stemmer
global result
result=[]
stemmer = SnowballStemmer("english")

def files_10():
    #Change number to select file
    count=7
    data = pd.read_csv('file' + str(count) + '.csv')
    df = pd.DataFrame(data)
    for index, c in df.iterrows():
        preprocess(c['"QUESTION' + str(count) + '"'])
    print(result)
    text = 'Question ' + str(count)
    with open(text, "w") as result_file:
        result_file.write('')
    dictionary = gensim.corpora.Dictionary(result)
    bow_corpus = [dictionary.doc2bow(doc) for doc in result]
    bow_doc_x = bow_corpus[0]
    for i in range(len(bow_doc_x)):
        print("Word {} (\"{}\") appears {} time.".format(bow_doc_x[i][0], 
                                                         dictionary[bow_doc_x[i][0]], 
                                                         bow_doc_x[i][1]))
    lda_model =  gensim.models.LdaMulticore(bow_corpus, 
                       num_topics = 6, 
                       id2word = dictionary,                                    
                       passes = 10,
                       workers = 2, per_word_topics=True)
    
    for idx, topic in lda_model.print_topics(-1):
        with open(text, "a") as result_file:
            result_file.write("Topic: {} \nWords: {}".format(idx, topic ) + "\n")
    vis = pyLDAvis.gensim.prepare(topic_model=lda_model, corpus=bow_corpus, dictionary=dictionary)
    pyLDAvis.enable_notebook()
    pyLDAvis.show(vis)
    
def stemming(i):
    i = stemmer.stem(WordNetLemmatizer().lemmatize(i, pos='v'))
    return i

def preprocess(stemma1):
    one = []
    for token in simple_preprocess(stemma1) :
        if token not in STOPWORDS and len(token) > 2:
            one.append(stemming(token))   
    return result.append(one)

files_10()



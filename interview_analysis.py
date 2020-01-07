import word2vec, os
import pandas as pd
from gensim.models import Word2Vec

global directory
directory = os.getcwd()

# Each question is assessed individually
def files_10():
    count = 1
    while count < 11:
        for i in os.listdir(directory):
            if i == 'text' + str(count):  
                text = "text" + str(count) + "-adapted" 
                vec = "text" + str(count) + "-vec.bin"
                cluster = "text" + str(count) + "-clusters.txt" 
                result = "text" + str(count) + "-result.txt" 
                #result_list = []
                stopwordsss = ["in", "it", "as", "my", "do", "is", "don't", "doesn't", "am", "it's", "i", "you", "and", "to", "the", "on", "but", "that", "are", "so", "to", "me", "of", "with", "try", 'a', 'about', 'after', 'all', 'also', 'always', 'am', 'an', 'and', 'any', 'are', 'at', 'be', 'been', 'being', 'but', 'by', 'came', 'can', "can't", 'come', 'could' , 'did', 'do', 'does', 'doing', 'else', 'for', 'from', 'get', 'give', 'goes', 'going', 'had', 'happen', 'has', 'have', 'having', 'how', 'in', 'into', 'really', 'if', 'see', 'plus', 'then',  "i'll", "then", "or", "will", "i'm", "too", "doesn't", "don't", "will", "that's", "-", "i've", "would", "making", "usually", "what", "hasn't", "it's", "hmmm", "really", "this", "someone", "not", "i'll", "like", "this", "e", "=", "just", "more", "actually", "most", "one", ":", "very", "b", "yes", "same"]                                                                       
                word2vec.word2phrase(i, text, verbose=True)
                #model = word2vec.load(vec)
                reading = open(text).read().lower().replace(',', ' ').replace('.', ' ').replace('/', ' ').replace('-', ' ').replace('(', ' ').replace(')', ' ').replace('?', ' ').split()
                for i in stopwordsss:
                    try:
                        reading = list(filter(lambda x: x != i, reading))
                    except:
                        continue
                print(reading)
                iterat = 0
                s = ' '
                s = s.join(reading)
                with open(text, "w") as result_file:
                    result_file.write(s)
                word2vec.word2vec(text, vec, 100, verbose=True)
                word2vec.word2clusters(vec, cluster, 100, verbose=True)
                for word in reading:
                    word2vec_model = Word2Vec([reading], min_count=1)
                    vocabulary = word2vec_model.wv.vocab
                    sim_words = word2vec_model.wv.most_similar(word)[:3]
                    #indexes, metrics = model.similar(word.lower())
                    #real_time = model.generate_response(indexes, metrics).tolist()
                    #result_list.append(sim_words)
                    #result_list.append('\n\n')
                    if iterat == 0:
                        with open(result, "w") as result_file:
                            result_file.write(str(word) + '\n' + str(sim_words) + '\n\n')
                        iterat = 1
                    elif iterat == 1:
                        with open(result, "a") as result_file:
                            result_file.write(str(word) + '\n' + str(sim_words) + '\n\n') 
                count += 1
            else:
                continue

# 2 Questions are united into 1
def files_5():
    count2 = 1
    while count2 < 11:
        for i in os.listdir(directory):
            if i == 'text' + str(count2) + '-' + str(count2 + 1):  
                text = "text" + str(count2) + "-adapted" 
                vec = "text" + str(count2) + "-vec.bin"
                cluster = "text" + str(count2) + "-clusters.txt" 
                result = "text" + str(count2) + "-result.txt" 
                #result_list = []
                stopwordsss = ["in", "it", "as", "my", "do", "is", "don't", "doesn't", "am", "it's", "i", "you", "and", "to", "the", "on", "but", "that", "are", "so", "to", "me", "of", "with", "try", 'a', 'about', 'after', 'all', 'also', 'always', 'am', 'an', 'and', 'any', 'are', 'at', 'be', 'been', 'being', 'but', 'by', 'came', 'can', "can't", 'come', 'could' , 'did', 'do', 'does', 'doing', 'else', 'for', 'from', 'get', 'give', 'goes', 'going', 'had', 'happen', 'has', 'have', 'having', 'how', 'in', 'into', 'really', 'if', 'see', 'plus', 'then',  "i'll", "then", "or", "will", "i'm", "too", "doesn't", "don't", "will", "that's", "-", "i've", "would", "making", "usually", "what", "hasn't", "it's", "hmmm", "really", "this", "someone", "not", "i'll", "like", "this", "e", "=", "just", "more", "actually", "most", "one", ":", "very", "b", "yes", "same"]                                                                       
                word2vec.word2phrase(i, text, verbose=True)
                #model = word2vec.load(vec)
                reading = open(text).read().lower().replace(',', ' ').replace('.', ' ').replace('/', ' ').replace('-', ' ').replace('(', ' ').replace(')', ' ').replace('?', ' ').replace('"', ' ').split()
                for i in stopwordsss:
                    try:
                        reading = list(filter(lambda x: x != i, reading))
                    except:
                        continue
                print(reading)
                iterat = 0
                s = ' '
                s = s.join(reading)
                with open(text, "w") as result_file:
                    result_file.write(s.replace('"', ' '))
                word2vec.word2vec(text, vec, 100, verbose=True)
                word2vec.word2clusters(text, cluster, 100, verbose=True)
                for word in reading:
                    word2vec_model = Word2Vec([reading], min_count=1)
                    vocabulary1 = word2vec_model.wv.vocab
                    sim_words = word2vec_model.wv.most_similar(word)[:3]
                    #indexes, metrics = model.similar(word.lower())
                    #real_time = model.generate_response(indexes, metrics).tolist()
                    #result_list.append(sim_words)
                    #result_list.append('\n\n')
                    if iterat == 0:
                        with open(result, "w") as result_file:
                            result_file.write(str(word) + '\n' + str(sim_words) + '\n\n')
                        iterat = 1
                    elif iterat == 1:
                        with open(result, "a") as result_file:
                            result_file.write(str(word) + '\n' + str(sim_words) + '\n\n') 
                count2 += 2
            else:
                continue

def launch():
    #files_10()
    files_5()
    
launch()
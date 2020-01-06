import word2vec, os
import pandas as pd
from gensim.models import Word2Vec

file = pd.read_csv("research.csv")
directory = os.getcwd()
count = 1
while count < 11:
    for i in os.listdir(directory):
        if i == 'text' + str(count):  
            text = "text" + str(count) + "-adapted" 
            vec = "text" + str(count) + "-vec.bin"
            cluster = "text" + str(count) + "-clusters.txt" 
            result = "text" + str(count) + "-result.txt" 
            result_list = []
            stopwordsss = ["in", "it", "as", "my", "do", "is", "don't", "doesn't", "am", "it's", "i", "you", "and", "to", "the", "on", "but", "that", "are", "so", "to", "me", "of", "with", "try"]
            word2vec.word2phrase(i, text, verbose=True)
            word2vec.word2vec(i, vec, 100, verbose=True)
            word2vec.word2clusters(text, cluster, 100, verbose=True)
            model = word2vec.load(vec)
            reading = open(text).read().lower().replace(',', ' ').replace('.', ' ').split()
            for i in stopwordsss:
                try:
                    reading = list(filter(lambda x: x != i, reading))
                except:
                    continue
            print(reading)
            iterat = 0
            for word in reading:
                word2vec_model = Word2Vec([reading], min_count=1)
                vocabulary = word2vec_model.wv.vocab
                sim_words = word2vec_model.most_similar(word)[:4]
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
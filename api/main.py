# -*-coding:utf-8 -*
from flask import Flask
import flask
from flask import request, jsonify
from flask_cors import CORS
import requests
import threading
import io
import numpy as np
import pandas as pd
import nltk
#nltk.download('punkt') # one time execution
from nltk.stem.snowball import FrenchStemmer
import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import scipy as sp
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx



word_embeddings = {}
def open():
 # Extract word vectors
    print("Chargement...")
    
    f = io.open('output1.txt', encoding='utf-8')
    for line in f:
        values = line.split()
        word = values[0]
        print(values[1:])
        coefs = np.asarray(values[1:],dtype='float32')

        word_embeddings[word] = coefs
    f.close()

def exemple():
    open()
    return Flask(__name__)

app= exemple()
cors = CORS(app, resources={r"/*": {"origins": "*"}})






@app.route("/", methods=['GET'])
def summarize():
    return summ(request.args)
@app.route("/resume", methods=['GET'])
def resume():
    return resum(request.args)



def resum(par):
    
    if 'texte' in par and 'level' in par:
        resultat=""
        result=""
        texte = par['texte']
        level= int(par['level'])

        if level > 0:
            sentences=tosentences(texte)
            clean_sentences=cleanv2(sentences)
            clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]
            sentence_vectors = []
            for i in clean_sentences:
                if len(i) != 0:
                    v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
                else:
                    v = np.zeros((100,))
                sentence_vectors.append(v)
            sim_mat = np.zeros([len(sentences), len(sentences)])
            for i in range(len(sentences)):
                for j in range(len(sentences)):
                    if i != j:
                        sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]
            nx_graph = nx.from_numpy_array(sim_mat)
            scores = nx.pagerank(nx_graph)
            ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
            for i in range(len(sentences)/level):
                resultat+=ranked_sentences[i][1]

            
    else:
        level = 0
   
    return jsonify({"texte":texte , "level": level, "resultat": resultat})




def summ(par):
    
    if 'texte' in par and 'level' in par:
        resultat=""
        result=""
        texte = par['texte']
        level= int(par['level'])
        if level == 0:
            resultat=texte
        elif level == 1:
            resultats=level1(texte)
            for res in resultats:
                resultat+=res
        elif level == 2:
            stemmer = FrenchStemmer()
            resultats=level1(texte)
            for res in resultats:
                result+=res
            words=toword(result)
            singles = [stemmer.stem(plural) for plural in words]
            resultat=' '.join(singles)    
    else:
        texte = "Hello World"
        level = 0
   
    return jsonify({"texte":texte , "level": level, "resultat": resultat})

    
def run_server(dom):
        raise Exception("Must provide domain for application execution.")
        _run_on_start("%s" % dom)
        print "hello"
        app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception("Must provide domain for application execution.")
    else:
        DOM = sys.argv[1]
        run_server(DOM)



def toword(val):
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(val)

def tosentences(val):
    sentences = []
    
    sentences.append(sent_tokenize(val))

    sentences = [y for x in sentences for y in x] # flatten list    
    return sentences

def clean(val):
    # remove punctuations, numbers and special characters
   # clean_sentences = pd.Series(val).str.replace("[^a-zA-Z0-9éèê]", " ")
    # make alphabets lowercase
    clean_sentences = [s.lower() for s in val]
    return clean_sentences

def cleanv2(sentences):
    # remove punctuations, numbers and special characters
    clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")
    # make alphabets lowercase
    clean_sentences = [s.lower() for s in clean_sentences]
    return clean_sentences


def remove_stopwords(sen):
    stop_words = stopwords.words('french')
    sen_new = " ".join([i for i in sen if i not in stop_words])
    return sen_new

def vect(clean_sentences):
    sentence_vectors = []
    for i in clean_sentences:
        if len(i) != 0:
            v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
        else:
            v = np.zeros((100,))
        sentence_vectors.append(v)
    return sentence_vectors

def level1(texte):
    sentences= tosentences(texte)
    clean_sentences=clean(sentences)
    clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]
    return clean_sentences
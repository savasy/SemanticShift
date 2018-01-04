import os
import gensim 
from gensim import corpora, models, similarities
from gensim.corpora import WikiCorpus, MmCorpus
from gensim.corpora import dictionary
import logging
from gensim.models.word2vec import BrownCorpus, Word2Vec
from gensim.models import Phrases
import nltk, os

def offset(pair):
 if pair[0] in model.vocab: 
  if pair[1] in model.vocab:
   return model[pair[0]] - model[pair[1]]
  else: 
   print(pair[1]+" missing")
   return []
 print(pair[0]+" missing")
 return []

def toStr(offs):
 s=""
 for o in offs:
  s=s+ ","+ str('%f' % o)
 return s

SIZE=300
modelName="sg0HS0Size"+str(SIZE)
model=Word2Vec.load("models/"+modelName)


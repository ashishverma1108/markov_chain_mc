#!usr/bin/env python
# encoding: utf-8

import nltk
import random
from collections import defaultdict

class transition_matrix(object):
    def __init__(self, corpus, n_grams):
        self.grams = {}
        self.corpus = corpus
        self.n_grams = n_grams
    #    self.sequences()


    def tokenizer(self, sentence, gram):
        tokenized_sentence = nltk.word_tokenize(sentence)
#        print self.n_grams
#        print "length of gram :%d" % gram#
#        print "length of tokenized_sentence: %d" % len(tokenized_sentence)
        if len(tokenized_sentence) < gram:
        #    print "here"
            pass
        else:
            for i in range(len(tokenized_sentence)-gram):
                yield(tokenized_sentence[i:i+gram+1])

    def sequences(self):
    #    print "inside sequences"
        for gram in range(1, self.n_grams+1):
        #    print "inside first loop"
            dictionary = {}
            for sentence in self.corpus:
            #    print "inside second loop"
                for sequence in self.tokenizer(sentence, gram):
                #    print sequence
                    key_id = tuple(sequence[0:-1])
                #    print key_id
                    if key_id in dictionary:
                    #    print dictionary
                    #    print key_id
                        dictionary[key_id].append(sequence[gram])
                    else:
                        dictionary[key_id] = [sequence[gram]]
            self.grams[gram] = dictionary
        return self.grams





if __name__ == '__main__':
    corpus = ["This is awesome.", "This is so awesome."]
    T_mat = transition_matrix(corpus, 2)
    possibilities = T_mat.sequences()
    print possibilities

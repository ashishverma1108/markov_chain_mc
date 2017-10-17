#!usr/bin/env python
# encoding: utf-8

from transition_matrix import transition_matrix
import random
import pandas
import csv
import re


#Genetrates sentence based on one word provided

class markovit(object):
    def __init__(self, _word, grams, min_length = 2):
        self._word = _word
        self.grams = grams
        self.min_length = 2

    def next_word(self, key_id):
#        key_id = tuple([key_id])
#        print type(key_id)
#        print len(self.grams[len(key_id)][key_id])

        for i in range(len([key_id])):
            try:
                if len(self.grams[len(key_id)][key_id]) >= 2:
#                    print random.choice(self.grams[len(key_id)][key_id])
                    return random.choice(self.grams[len(key_id)][key_id])
            except KeyError:
                pass
    #        print "here"
            ### Cut down key_id if the current version didn't return next word
            ###  that met min_length requirement
    #        print key_id[1:]
            if len(key_id) > 1:
                key_id = key_id[1:]
                print key_id
            try:
                return random.choice(self.grams[len(key_id)][key_id])
            except KeyError:
#                print "here 1"
#                return random.choice(' '.join(self.grams).encode('utf-8').strip().split())
                return random.choice(self.grams[1][tuple(["this"])])

    def next_key(self, key_id, result):
        key_id = tuple([key_id])
#        print tuple(key_id[1:]) + tuple([result])
        return tuple(key_id[1:]) + tuple([result])

    def generate_markov_text(self, _word):
        key_id = tuple([self._word])
        #print key_id[]]
        gen_words = []
        gen_words.append(key_id[0])
#        print gen_words
        word_count = 0
        result = "a"
        while result != ".":      #word_count <= 2:
    #        print key_id
            result = self.next_word(key_id)
    #        print result
            key_id = self.next_key(key_id, result)
            gen_words.append(result)
            if result == ".":
                word_count = word_count + 1

        return gen_words


if __name__ == '__main__':
    tweets = pandas.read_csv("realDonaldTrump_tweets.csv")
    final_tweets = tweets.loc[:,'text']
    final_tweets = final_tweets.values.T.tolist()
    final_tweets =  [re.sub(r"https://t.co/[a-zA-Z0-9]*", '', row, flags=re.MULTILINE)  for row in final_tweets]
    final_tweets =  [re.sub(r"\n", '', row, flags=re.MULTILINE)  for row in final_tweets]
    final_tweets = [line.decode('utf-8').strip() for line in final_tweets]
    _corpus = final_tweets
    _n_grams = 2
    _min_length = 2
    _t_mat = transition_matrix(_corpus, _n_grams)
    _t_mat_result = _t_mat.sequences()

    markov =markovit(random.choice(["This", "Russia", "The"]), _t_mat_result, _min_length )
    output_text = markov.generate_markov_text(random.choice(["This", "Russia", "The"]))
#    print "here 2"
    print ' '.join(output_text).encode('utf-8').strip().replace(' .','.').replace(' ,',',')

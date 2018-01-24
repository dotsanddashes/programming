import random

def open_file(fname):
    with open (fname, encoding = 'utf-8') as f:
        text = f.read()
        words_list = text.splitlines()
    return random.choice(words_list)

def noun():
    open_file('nouns.txt')
    return open_file('nouns.txt')

def adjective(word):
    open_file('adjectives.txt')
    return open_file('adjectives.txt') + ' ' + word

def adverb():
    open_file('adverbs.txt')
    return open_file('adverbs.txt')

def verb(subj, adv):
    open_file('verbs.txt')
    return subj + ' ' + adv + ' ' + open_file('verbs.txt')

def preposition():
    open_file('prepositions.txt')
    return open_file('prepositions.txt') + ' '

def random_sentence():
    sentence = verb(adjective(noun()), adverb()) + ', ' + preposition() + verb(adjective(noun()), adverb()) + '.'
    return sentence

num_of_sents = random.randint(5, 15)
for i in range(num_of_sents):
    sentence = random_sentence()
    sentence = sentence.capitalize()
    print(sentence, end=' ')
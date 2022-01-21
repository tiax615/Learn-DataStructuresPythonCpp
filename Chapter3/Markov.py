# 3.6.4 马尔可夫链
import random

class Markov:
    '''A simple trigram三元 Markov model. The current state is a sequence
       of the two words seen most recently. Initially, the state is
       (None, None), since on words have been seen. Scanning the
       sentence "The man ate the pasta" would cause the
       model to go through the sequence of states: [(None, None),
       (None, 'The'), ('The', 'man'), ('man', 'ate'), ('ate', 'the'),
       ('the', 'pasta')]'''

    def __init__(self):
        '''post: creates an empty Markov model with initial state
                 (None, None).'''
        self.model = {} # maps states to lists of words
        self.state = (None, None) # last two words processed
    
    def add(self, word):
        '''post: Adds word as a possible following word for current
                 state of the Markov model and sets state to
                 incorporate word as most recently seen.
           ex: If state was ('the', 'man') and word is 'ate' then
               'ate' is added as a word that can follow "... the man"
               and the state is now ('man', 'ate')'''
        if self.state in self.model:
            # we have an existing list of words for this state
            # just add this new one (word).
            self.model[self.state].append(word)
        else:
            # first occurence of this state, create a new list
            self.model[self.state] = [word]
        # transition to the next state given next word
        self._transition(word)

    def randomNext(self):
        '''post: Returns a random choice from among the possible choices
                 of next words, given the current state, and updates the
                 state to reflect the word produced.
           ex: If the current state is ("the", "man"), and the known
               next words are ["ate", "ran", "hit", "ran"], one of
               these is selected at random. Suppose "ran" is selected,
               then the new state will be: ("man", "ran"). Note the
               list of next words can contain duplicates so the
               relative frequency of a word in the list represents its
               probability of being the next word.'''
        # get list of next words for this state
        lst = self.model[self.state]
        # choose one at random
        choice = random.choice(lst)
        # transition to next state, given the word choice
        self._transition(choice)
        return choice

    def reset(self):
        '''post: The model state is reset to its initial
                 (None, None) state.
           note: This does not change the transition information that
                 has been learned so far (via add()), it
                 just resets the state so we can start adding
                 transitions or making predictions for a "fresh"
                 sequence.'''
        self.state = (None, None)

    def _transition(self, next):
        # help function to construct next state
        self.state = (self.state[1], next)

def makeWordModel(filename):
    # creates a Markov model from words in filename
    infile = open(filename)
    model = Markov()
    for line in infile:
        words = line.split()
        for w in words:
            model.add(w)
    infile.close()
    # Add a sentinel at the end of the text
    model.add(None)
    model.reset()
    return model

def generateWordChain(markov, n):
    # generates up to n words of output from a model
    words = []
    for i in range(n):
        next = markov.randomNext()
        if next is None: break # got to a final state
        words.append(next)
    return " ".join(words)

def main():
    markov = makeWordModel('Alice.txt')
    print(generateWordChain(markov, 10))

if __name__ == '__main__':
    main()
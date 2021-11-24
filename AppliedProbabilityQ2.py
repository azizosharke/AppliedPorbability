#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import random
random.seed(12345678)


def gameOfCard():
    cards = list(range(1, 101))
    np.random.shuffle(cards)  # will create deck of 100 cards randomly and then shuffle them
    noHits: int = 0
    for x in range(0, 100):
        if cards[x] != x+1:
            continue
        noHits += 1
    return noHits


def questionTwo():
    shuffle = np.array([cardGame()for x in range( 10000)])
    avg = sum(shuffle) / len(shuffle)
    var = sum((x - avg) ** 2 for x in shuffle) / len(shuffle)
    expectation = avg



    print(" | expectation of 10000 repititions| " + str(expectation))
    print(" | variance of  10000 repititions  |  " + str(var))


questionTwo()


# In[39]:


import random
random.seed(12345678)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def cardGame():
    cards = list(range(1, 101))
    random.shuffle(cards)           
    noHits = 0
    for x in range(0,100):
        if cards[x] == x+1:
             noHits+=1
    return noHits                      


def questionTwo():
    cardSet = np.array([cardGame()for x in range( 10000)])
    variance = np.var(cardSet)
    expectation = np.mean(cardSet)
    print(" | expectation of 10000 repititions| " + str(expectation))
    print(" | variance of  10000 repititions  |  " + str( variance))
    plt.plot([cardSet[:i+1].var() for i in range(10000)])
    plt.plot([cardSet[:i+1].mean() for i in range(10000)])
    
   

   

    plt.title("The variance and expectation of 10000 repetitions ")
 
    
    
questionTwo()


# In[20]:


import random
random.seed(12345678)
import numpy as np
import matplotlib.pyplot as plt


def cardGame():
    cards = list(range(1, 101))
    random.shuffle(cards)           
    hits = 0
    for x in range(0,100):
        if cards[x] == x+1:
            hits+=1
    return hits                      


def questionTwo():
    cardSet = np.array([cardGame()for x in range( 10000)])
    variance = np.var(cardSet)
    expectation = np.mean(cardSet)
    print(" | expectation of 10000 repititions| " + str(expectation))
    print(" | variance of  10000 repititions  |  " + str( variance))
    plt.plot([cardSet[:i+1].var() for i in range(10000)])

    plt.title("The variance of 10000 repetitions ")
questionTwo()


# In[19]:


import random
random.seed(12345678)
import numpy as np
import matplotlib.pyplot as plt


def cardGame():
    cards = list(range(1, 101))
    random.shuffle(cards)           
    hits = 0
    for x in range(0,100):
        if cards[x] == x+1:
            hits+=1
    return hits                      


def questionTwo():
    cardSet = np.array([cardGame()for x in range( 10000)])
    variance = np.var(cardSet)
    expectation = np.mean(cardSet)
    print(" | expectation of 10000 repititions| " + str(expectation))
    print(" | variance of  10000 repititions  |  " + str( variance))
   
   
    plt.plot([cardSet[:i+1].mean() for i in range(10000)])

    plt.title("The  expectation of 10000 repetitions ")
questionTwo()


# In[ ]:





import random

import numpy as np

def simulate_dice_rolls(num_trials):
    sum_equals_10_count = 0
    for _ in range(num_trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 + die2 == 10:
            sum_equals_10_count += 1
    return sum_equals_10_count / num_trials

# Number of trials
num_trials = 1000000  # Large number for better accuracy

# Perform the simulation
probability_sum_10 = simulate_dice_rolls(num_trials)
#print(f"The estimated probability that the sum is 10 is approximately: {probability_sum_10}")


'''
def build_word_dict(X, Y):
    word_dict = {}
    for i, email in enumerate(X):
        label = 'spam' if Y[i] == 1 else 'ham'
        for word in email:
            if word not in word_dict:
                word_dict[word] = {'spam': 0, 'ham': 0}
            word_dict[word][label] += 1
    return word_dict
'''
# Example data
X = np.array([["hello", "world"], ["buy", "now"], ["hello", "buy"]])
Y = np.array([0, 1, 1])  # 0: ham, 1: spam

def build_word_dict (X,Y):
    emails=X
    labels =Y
    word_dict={}
    for  i, email in  enumerate(emails):
        for word in email :
            word_dict[word] = {'spam':0,'ham':0}

    for   j ,email in  enumerate(emails):
        for word in email :
           if labels[j] == 0:
              word_dict[word]['spam'] +=1;
   
           elif labels[j]==1:
              word_dict[word]['ham'] +=1;      



    print(word_dict)               
                       
                      
X = np.array([["hello", "world"], ["buy", "now"], ["hello", "buy"]])
Y = np.array([0, 1, 1])  # 0: ham, 1: spam    

build_word_dict(X,Y)


# Parameters

#print(probability_sum_10)




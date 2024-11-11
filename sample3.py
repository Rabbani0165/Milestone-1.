import pandas as pd

file = open(r'C:\Users\Administrator\Desktop\UST_Training\Day_11\sample.csv','r')

word_freq = {}

for line in file:
    
    words = line.split()

    for word in words:
        if word:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

df = pd.DataFrame(word_freq.items(),columns=['word' , 'Frequency'])

print(df)

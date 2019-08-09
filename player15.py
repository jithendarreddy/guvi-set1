def most_frequent(text):
    frequencies = [(c, text.count(c)) for c in set(text)]
    return max(frequencies, key=lambda x: x[1])[0]

s = input()
print(most_frequent(s))
    
    

import math

def kaisiski_test(cipher):
    
    # bigram frequency
    bigrams = {}
    for i in range(len(cipher) - 1):
        if cipher[i:i+2] not in bigrams:
            bigrams[cipher[i:i+2]] = [i]
        else:
            bigrams[cipher[i:i+2]].append(i)
    
    # find the distances between the bigrams
    distances = {}
    for bigram in bigrams:
        if len(bigrams[bigram]) > 1:
            distances[bigram] = []
            for i in range(len(bigrams[bigram]) - 1):
                distances[bigram].append(bigrams[bigram][i+1] - bigrams[bigram][i])

    # find the gcd of the distances
    gcd = 0
    for bigram in distances:
        for i in range(len(distances[bigram])):
            for j in range(i+1, len(distances[bigram])):
                gcd = math.gcd(distances[bigram][i], distances[bigram][j])
                if gcd > 1:
                    return gcd
    
    return gcd


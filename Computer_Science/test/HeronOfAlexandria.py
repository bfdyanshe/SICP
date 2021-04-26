
def averanginOfHOA(X, G):
    if abs(G - X/G) > 0.000000000000001:
        avg = (G+X/G)/2
        print(avg)
        averanginOfHOA(X, avg)
    else:
        print(G)


averanginOfHOA(2, 1)

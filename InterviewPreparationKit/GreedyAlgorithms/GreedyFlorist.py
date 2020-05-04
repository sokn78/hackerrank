def getMinimumCost(k, c):
    sc = sorted(c, reverse = True)
    chunks = [sc[i*k:(i+1)*k] for i in range(0,len(sc//k))]
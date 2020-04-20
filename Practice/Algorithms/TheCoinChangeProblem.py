def getWays(n, c):
    solutions = dict()
    min_c = min(c)
    def get_nb_change(min_coin_added,n,c):
        if (min_coin_added,n) not in solutions:
            if n == 0:
                solution = 1
            elif n < min_coin_added:
                solution = 0
            else :
                solution = sum([get_nb_change(coin,n-coin,c) for coin in c if (coin <= n) & (coin >=min_coin_added)])
            solutions[(min_coin_added,n)] = solution
        return solutions[(min_coin_added,n)]
    return get_nb_change(min_c,n,c)
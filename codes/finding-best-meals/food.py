#!/usr/bin/env python3
import numpy as np # harness the power of matrices
import data
from data import utility
from collections import defaultdict
import pdb

def brute_force(products, labels, n, budget):
    numproducts = len(products)
    def combine(a,b,samearray=False):
            if a is None or b is None:
                return None
            res = np.array([])
            if not samearray:
                for rowi in a:
                    for rowj in b:
                        if res.shape != (0,):
                            res = np.vstack([res, rowi+rowj])
                        else:
                            res = rowi+rowj
            else:
                maxi = a.shape[0]
                maxj = b.shape[0]
                for i in range(maxi):
                    for j in range(i, maxj):
                        if res.shape != (0,):
                            res = np.vstack([res, a[i,:]+b[j,:]])
                        else:
                            res = a[i,:] + b[j,:]
            return res
    def enumerate_cases(products, budget):
        # find smallest price difference
        prices = [p.price for p in products]
        prices, size = sorted(prices), len(prices)
        diffs = [prices[i + 1] - prices[i] for i in range(size) if i+1 < size]
        step = min(diffs)
        minprice = prices[0]
        unlocked = {}
        combinations = defaultdict(dict)
        def all_cases(b, selector=None):
            stack = []
            b_unlocked = unlocked.get(b)
            if not b_unlocked is None:
                stack.append(b_unlocked)
            b_combinationdict = combinations.get(b)
            if not b_combinationdict is None:
                if selector is None:
                    b_combination = np.vstack([p[1] for p in b_combinationdict.items()])
                else:
                    b_combination = b_combinationdict.get(selector)
                if not b_combination is None:
                    stack.append(b_combination)
            if stack != []:
                return np.vstack(stack)
            else:
                return None


        for b in np.arange(minprice, budget+step, step):
            # unlocked items
            b_unlocked = np.logical_and(prices<=b, prices>b-step)
            # new combinations
            b_combinations = np.array([])
            def pick_combine(array_a, array_b, samearray):
                combination = combine(array_a, array_b, samearray)
                if combination is not None:
                    if len(combination.shape) == 1:
                        combination = np.expand_dims(combination, axis=0)
                    combinations[b][budget_a] = combination

            budget_a = .5; budget_b = b-.5
            samearray = budget_a == budget_b
            pick_combine(all_cases(budget_a), all_cases(budget_b), samearray)

            if np.any(b_unlocked):
                unlocked[b] = np.expand_dims(b_unlocked.astype(int), axis=0)
            #if b_combinations.shape != (0,):
            #    combinations[b] = b_combinations
        print('Unlocked')
        for key, value in unlocked.items():
            print('{}: {}'.format(key, value))
        print('Combinations')
        for key, value in combinations.items():
            value = np.vstack([p[1] for p in value.items()])
            print('{}: {}'.format(key, value))
        pdb.set_trace()
    cases = enumerate_cases(products, budget)
    pdb.set_trace()
    print('{} cases to consider, oh boy!'.format(len(cases)))
    assert(len(cases) == pow(n+1, numproducts))
    cases = np.vstack((cases)) # put it into a matrix
    # vectorize products' information
    v = [p.to_vector() for p in products]

    def evaluate_cases(cases, products):
        m = np.vstack((v))
        # m is a p*5 matrix, cases is a X*p matrix
        result = np.matmul(cases, m)
        # calculate utility
        nutrients = result[:,0:4]
        utils = utility(nutrients)

        prices = result[:,4]
        return utils, prices

    utils,prices = evaluate_cases(cases, products)
    def best_case(cases, utils, prices, budget):
        inbudget = prices <= budget
        utils = utils[inbudget]
        prices = prices[inbudget]
        cases = cases[inbudget]
        indexmaxutil = np.argmax(utils)
        return cases[indexmaxutil], prices[indexmaxutil]

    bestcase, price = best_case(cases, utils, prices, budget)
    print('Ayt Miss. Here is your ${} meal:'.format(price))
    for x in range(len(bestcase)):
        if bestcase[x] > 0:
            print('    - {}: {} units'.format(products[x].name, bestcase[x]))
    nutrients = np.matmul(bestcase, v)[0:3]
    msg = 'It gives you'
    for i in range(len(nutrients)):
        msg = '{} {} {}'.format(msg, nutrients[i], labels[i])
    print(msg)

if __name__ == '__main__':
    # read product data
    products, labels = data.readfile('datasets/prices.csv')
    #budget = input('Input your max daily budget in dollars:\n>>')
    #budget = float(budget)
    budget = 3
    # BRUTE FORCE POWER
    brute_force(products, labels, 3, budget)


#!/usr/bin/env python3
import numpy as np # harness the power of matrices
import data
from data import utility
from collections import defaultdict
import pdb

def brute_force(products, labels, budget, desiredpercent):
    numproducts = len(products)
    prices = [p.price for p in products]
    def combine(i,j):
        res = []
        for x in i:
            for y in j:
                res.append(np.hstack((x,y)))
        return res
    def enumerate_cases(p,n):
        choices = np.arange(n+1)
        res = choices
        for i in range(p-1):
            res = combine(choices, res)
        return res
    n = budget / min(prices)
    cases = enumerate_cases(numproducts, n)
    # filter cases that cost more than budget
    def filter_cases(unfilteredcases):
        filteredcases = []
        for case in cases:
            price = np.matmul(case, prices)
            if price <= budget:
                filteredcases.append(case)
        return np.vstack(filteredcases)
    cases = filter_cases(cases)
    print('{} cases to consider, okay!'.format(len(cases)))
    cases = np.vstack((cases)) # put it into a matrix
    # vectorize products' information
    v = [p.to_vector() for p in products]

    def evaluate_cases(cases, products):
        m = np.vstack((v))
        # m is a p*5 matrix, cases is a X*p matrix
        result = np.matmul(cases, m)
        # calculate utility
        nutrients = result[:,0:4]
        utils = utility(nutrients, desiredpercent)

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
        msg = '%s %.0f%% %s' % (msg, nutrients[i], labels[i])
    msg = msg + ' of your daily intake'
    print(msg)

if __name__ == '__main__':
    # read product data
    products, labels = data.readfile('datasets/starmarket.csv')
    budget = input('What is your max daily budget in dollars?\n>>')
    budget = float(budget)

    calories =input('What is your desired daily calorie intake?\n>>')
    calories = float(calories)

    desiredpercent = (calories / 2000) * 100
    # BRUTE FORCE POWER
    brute_force(products, labels, budget, desiredpercent)


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
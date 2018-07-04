import csv
import numpy as np
import pdb

class Product(object):
    def __init__(self, name, fat, carbs, protein, servings, price):
        self.name = name
        self.servings = servings
        self.fat = fat * servings
        self.carbs = carbs * servings
        self.protein = protein * servings
        self.price = price

    def to_vector(self):
        return np.array([self.fat, self.carbs,
            self.protein, self.servings, self.price])

def readfile(path):
    products = []
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        labels = next(reader) #first line is labels
        for row in reader:
            product = Product(row[0],
                            float(row[1]),
                            float(row[2]),
                            float(row[3]),
                            float(row[4]),
                            float(row[5]))
            products.append(product)
    labels = labels[1:-2] # remove non-nutritional info
    return products, labels

def utility(rows, desiredpercent):
    # calculates utility as in Eqn.1 in the article
    # rows: a matrix whose columns is daily percentages of nutrients eaten.
    perfectrow = [desiredpercent] * rows.shape[1]
    result = -np.absolute(rows - perfectrow)
    return np.sum(result, axis=1)

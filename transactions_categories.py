from typing import List
from collections import defaultdict
from transaction import *
from category import *


from sortedcontainers import SortedDict


class TransactionsAndCategories:
    def __init__(self, transactions, categories):
        self.transactions = SortedDict()
        self.categories = {}

        self.init(transactions, categories)

    def init(self, transactions, categories):
        for tran in transactions:
            if tran.id in self.transactions:
                raise Exception(
                    'Transaction provided with same id, make sure all ids are unique')
            else:
                self.transactions[tran.id] = tran

        for cat in categories:
            if cat.id in self.categories:
                raise Exception(
                    'Category provided with same id, make sure all ids are unique')
            else:
                self.categories[cat.id] = cat

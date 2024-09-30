from transactions_categories import *
from notifications import *
from notification import *
from category import *
from transaction import *
from spent_category import *
from spent_category_tree import *
import random
from collections import defaultdict, deque
from datetime import datetime, timedelta
# Initialize global instances
transactions_and_categories = TransactionsAndCategories([], [])
spent_category_tree = SpentCategoryTree()
notifications_queue = NotificationsQueue()


def main():
    # Initialize categories
    categories = [
        Category(id=0, title='Grocery',
                 description='Groceries we buy from stores'),
        Category(id=1, title='Movies', description='Movie ticket costs'),
        Category(id=2, title='Electronics',
                 description='Electronic items we buy'),
        Category(id=3, title='Gas',
                 description='Gasoline added for our vehicles'),
        Category(id=4, title='Food', description='Foods we have at restaurants')
    ]

    # Generate random transactions
    sample_transactions = []
    for i in range(200):
        category_id = random.randint(0, 4)
        sample_transactions.append(
            Transaction(
                id=i,
                amount=random.uniform(0, 1000),
                category_id=category_id,
                title=f'{categories[category_id].title} transaction #{i}',
                description=f'{categories[category_id].description}',
                transaction_dt=datetime.now() - timedelta(days=random.randint(0, 60)),
            )
        )

    build_app(sample_transactions, categories)

    highest_spent = spent_category_tree.get_highest_spent_category()
    if highest_spent:
        print(
            f'Highest spent category: {highest_spent} Category: {transactions_and_categories.categories[highest_spent.category_id]}')

    print('All spent amounts:\n ' +
          '\n'.join(map(str, spent_category_tree.get_all_items())))
    print('Minimum spent category: ' + str(spent_category_tree.find_minimum()))

    print('Lets run the notifications')


def build_app(transactions: list[Transaction], categories: list[Category]):
    global transactions_and_categories, spent_category_tree, notifications_queue

    transactions_and_categories = TransactionsAndCategories(
        transactions, categories)
    spent_on_categories = {}
    id_counter = 0
    budget_limit = 100.0  # Random budget limit for grocery and food category

    for tran in transactions:
        if tran.category_id in spent_on_categories:
            spent_on_categories[tran.category_id].amount += tran.amount
        else:
            spent_on_category = SpentOnCategory(
                id=id_counter,
                amount=tran.amount,
                category_id=tran.category_id,
                budget_limit=budget_limit if tran.category_id in (
                    0, 4) else SpentOnCategory.NO_BUDGET_LIMIT,
            )
            spent_on_categories[tran.category_id] = spent_on_category
            if spent_on_category.amount >= budget_limit:
                notifications_queue.add_notification(
                    Notification(
                        priority=random.randint(0, 100),
                        id=random.randint(0, 100),
                        title=f'{transactions_and_categories.categories[spent_on_category.category_id].title} limit exceeded',
                        description=f'Budget Limit exceeded for {transactions_and_categories.categories[tran.category_id].title}',
                    )
                )
            id_counter += 1

    spent_category_tree.build_tree(spent_on_categories)


if __name__ == "__main__":
    main()

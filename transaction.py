from datetime import datetime


class Transaction:
    def __init__(self, id: int, amount: float, category_id: int, title: str, description: str, transaction_dt: datetime):
        self.id = id
        self.amount = amount
        self.category_id = category_id
        self.title = title
        self.description = description
        self.transaction_dt = transaction_dt

    def __repr__(self):
        return (f"Transaction(id: {self.id}, amount: {self.amount}, "
                f"category_id: {self.category_id}, title: {self.title}, "
                f"description: {self.description}, transaction_dt: {self.transaction_dt})")

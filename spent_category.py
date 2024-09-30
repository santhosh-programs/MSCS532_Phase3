class SpentOnCategory:
    # Default budget limit of -1 if no budget limit is set
    NO_BUDGET_LIMIT = -1.0

    def __init__(self, id: int, amount: float, category_id: int, budget_limit: float = NO_BUDGET_LIMIT):
        self.id = id
        self.amount = amount
        self.category_id = category_id
        self.budget_limit = budget_limit

    def __repr__(self):
        return (f"SpentOnCategory(id: {self.id}, amount: {self.amount}, "
                f"category_id: {self.category_id}, budget_limit: {self.budget_limit})")

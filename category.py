class Category:
    def __init__(self, id: int, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description

    def __repr__(self):
        return f"Category(id: {self.id}, title: {self.title}, description: {self.description})"


# Example usage:
category = Category(id=1, title="Groceries",
                    description="Monthly grocery shopping")
print(category)

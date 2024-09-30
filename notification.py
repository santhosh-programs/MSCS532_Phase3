class Notification:
    def __init__(self, id, title, description, priority):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority

    def __str__(self):
        return f'Notification(id: {self.id}, title: {self.title}, description: {self.description}, priority: {self.priority})'

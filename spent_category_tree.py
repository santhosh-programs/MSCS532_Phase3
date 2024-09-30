from spent_category import *


class Color:
    RED = "RED"
    BLACK = "BLACK"


class SpentCategoryNode:
    def __init__(self, spent_on_category, color=Color.RED):
        self.spent_on_category = spent_on_category
        self.color = color
        self.left_child = None
        self.right_child = None


class SpentCategoryTree:
    def __init__(self):
        self.root_node = None

    def build_tree(self, spent):
        for key, value in spent.items():
            self.insert(value)

    def get_highest_spent_category(self):
        return self.root_node.spent_on_category if self.root_node else None

    def insert(self, item):
        self.root_node = self._insert(self.root_node, item)
        if self.root_node:
            self.root_node.color = Color.BLACK

    def _insert(self, node, item):
        if node is None:
            return SpentCategoryNode(spent_on_category=item)

        if item.amount < node.spent_on_category.amount:
            node.left_child = self._insert(node.left_child, item)
        elif item.amount > node.spent_on_category.amount:
            node.right_child = self._insert(node.right_child, item)
        else:
            return node  # No duplicates allowed

        return self._fix_up(node)

    def _fix_up(self, node):
        if self._is_red(node.right_child):
            node = self._rotate_left(node)

        if self._is_red(node.left_child) and self._is_red(node.left_child.left_child):
            node = self._rotate_right(node)

        if self._is_red(node.left_child) and self._is_red(node.right_child):
            self._flip_colors(node)

        return node

    def _is_red(self, node):
        return node is not None and node.color == Color.RED

    def _rotate_left(self, node):
        x = node.right_child
        node.right_child = x.left_child
        x.left_child = node
        x.color = node.color
        node.color = Color.RED
        return x

    def _rotate_right(self, node):
        x = node.left_child
        node.left_child = x.right_child
        x.right_child = node
        x.color = node.color
        node.color = Color.RED
        return x

    def _flip_colors(self, node):
        node.color = Color.RED
        if node.left_child:
            node.left_child.color = Color.BLACK
        if node.right_child:
            node.right_child.color = Color.BLACK

    def find_spent_amount(self, category_id):
        return self._find_node_by_category_id(self.root_node, category_id)

    def increase_amount(self, amount, category_id):
        return self._change_amount(amount, category_id)

    def decrease_amount(self, amount, category_id):
        return self._change_amount(-amount, category_id)

    def _change_amount(self, amount, category_id):
        item = self._find_node_by_category_id(self.root_node, category_id)
        if item:
            item.amount += amount
            return True
        return False

    def _find_node_by_category_id(self, node, category_id):
        if node is None:
            return None
        if category_id == node.spent_on_category.categoryId:
            return node.spent_on_category
        found_in_left = self._find_node_by_category_id(
            node.left_child, category_id)
        if found_in_left:
            return found_in_left
        return self._find_node_by_category_id(node.right_child, category_id)

    def get_all_items(self):
        return self._in_order_traversal(self.root_node)

    def _in_order_traversal(self, node):
        result = []
        if node is None:
            return result
        result.extend(self._in_order_traversal(node.left_child))
        result.append(node.spent_on_category)
        result.extend(self._in_order_traversal(node.right_child))
        return result

    def find_minimum(self):
        return self._find_minimum(self.root_node).spent_on_category if self.root_node else None

    def _find_minimum(self, node):
        while node and node.left_child is not None:
            node = node.left_child
        return node

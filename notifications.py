from collections import deque
# Ensure this import points to your Notification class
from notification import Notification


class NotificationsQueue:
    def __init__(self):
        self.heap = []

    def add_notification(self, notification):
        self.heap.append(notification)
        self._heapify_up(len(self.heap) - 1)

    def get_highest_priority_notification(self):
        if not self.heap:
            return None

        self._swap(0, len(self.heap) - 1)
        # remove last item (highest priority)
        highest_priority_notification = self.heap.pop()

        self._heapify_down(0)

        return highest_priority_notification

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2

        if index > 0 and self.heap[index].priority > self.heap[parent_index].priority:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index].priority > self.heap[largest].priority:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index].priority > self.heap[largest].priority:
            largest = right_child_index

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

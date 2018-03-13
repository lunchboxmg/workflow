import heapq

class InputManager(object):

    def __init__(self):

        self._data = []

class TaskNode(object):

    AVG = 1.0
    STD = 1.0

    def __init__(self, numQueues):

        self._queues = [[] for _ in xrange(numQueues)]

if __name__ == "__main__":

    # Test Case
    ops = [TaskNode() for _ in xrange(NUM)]

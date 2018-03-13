import heapq

class InputManager(object):

    def __init__(self):

        self._data = []

class TaskNode(object):

    AVG = 1.0
    STD = 1.0

    def __init__(self, numQueues):

        self._queues = [[] for _ in xrange(numQueues)]

class NodeManager(object):
    """ Master container for all the various created nodes. """

    signals = []
    intercepts = []

class SignalNode(object):
    """ Contains all the information / parameters for a signal. """

    _COUNT = 0 # Internal counter for indexing

    def __init__(self, uid, key=None):
        """ Constructor. """

        # Index and save
        self._index = SignalNode._COUNT
        SignalNode._COUNT += 1
        NodeManager.signals.append(self)

        # Parameters
        self._uid = uid
        self._key = key

    def get_index(self): return self._index

    def get_uid(self): return self._uid

    def get_key(self): return self._key

class InterceptNode(object):
    """ Collection of timing information pertaining to the capture of signal
    events.  This class is useful for connecting various takes together. """

    _COUNT = 0 # Internal counter for indexing

    def __init__(self, sig_index, time_start, time_stop):
        """ Constructor. """

        # Index and save
        self._index = InterceptNode._COUNT
        InterceptNode._COUNT += 1
        NodeManager.intercepts.append(self)

        # Parameters
        self._sig_index = sig_index
        self._time_start = time_start
        self._time_stop = time_stop

    def get_index(self): return self._index

    def get_sig_index(self): return self._sig_index

    def get_signal(self): return NodeManager.signals[self._sig_id]

    def get_time_start(self): return self._time_start

    def get_time_stop(self): return self._time_stop

    def get_duration(self): return self._time_stop - self._time_start


if __name__ == "__main__":

    # Test Case
    ops = [TaskNode() for _ in xrange(NUM)]

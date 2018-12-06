class QueueNode(object):
    """ Node: Class for single node of LinkedQueue """

    def __init__(self, elem, nextnode):
        self.elem = elem
        self.nextnode = nextnode
        """ Initializes new node """


class QueueIterator(object):
    """ QueueIterator: Iterator for LinkedQueue """

    def __init__(self, node, emptynode):
        self.node = node
        self.emptynode = emptynode
        """ Initializes new Iterator """

    def __next__(self):
        """ Returns next element of queue: next(iter) """
        if self.node is True:
            raise StopIteration
        else:
            node = self.node.elem
            self.node =  self.node.nextnode
            self.emptynode -= emptynode

        return node, emptynode


class LinkedQueue:
    """ LinkedQueue """

    def __init__(self):
        """ Initializes new queue """
        self.add = None
        self.node = None
        self.emptynode = 0


    def push(self, elem):
        """ Pushes 'elem' to queue """
        if not self.emptynode:
            self.add = QueueNode(elem, None)
            self.node = self.add
            self.emptynode = 1
        else:
            new_node = QueueNode(elem, None)
            self.add.next = new_node
            self.add = new_node
            self.emptynode += 1

    def pop(self):
        """ Removes front of queue and returns it """
        node = self.node.elem
        self.node = self.node.next
        self.emptynode -= 1
        return node

    def front(self):
        """ Returns front of queue """
        return self.node.elem

    @property
    def empty(self):
        """ Checks whether queue is empty """
        if not emptynode:
            return True
        else:
            return False

    def __iter__(self):
        """ Returns Iterator for queue: iter(queue) """
        return QueueIterator(self.node, self.emptynode)

    def __len__(self):
        """ Returns size of queue: len(queue) """
        return self.emptynode

    def clear(self):
        """ Makes queue empty """
        self.add = None
        self.node = None
        self.emptynode = 0
        
        #### TESTING ####

def main():
    q = LinkedQueue()
    print(q.push(1))
    print(q.push(2))
    print(q.push(10))
    print(len(q))  # 3
    print(q.pop())  # 1
    print(q.pop())  # 2
    print(len(q))  # 1
    print(q.clear())
    print(len(q))  # 0

main()


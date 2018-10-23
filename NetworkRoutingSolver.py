#!/usr/bin/python3


from CS312Graph import *
import time


class NetworkRoutingSolver:
    def __init__(self):
        pass

    def initializeNetwork(self, network):
        assert (type(network) == CS312Graph)
        self.network = network

    def getShortestPath(self, destIndex):
        self.dest = destIndex
        nodesList = self.network.getNodes()

        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL
        #       NEED TO USE
        path_edges = []
        myEdges = self.network.getEdges()
        dest = nodesList[destIndex]
        total_length = dest.getDistance()
        shortestPath = []
        dest = destIndex
        prev = None
        while prev != self.source:
            destination = nodesList[dest]
            previous = destination.getPrev()
            if previous == None:
                total_length = "Unreachable"
                return {'cost': total_length, 'path': []}
            prev = previous.getId()
            neighbors = myEdges[prev]
            for neighbor in neighbors:
                if neighbor[0] == dest:
                    newEdge = (previous.loc, destination.loc, '{:.0f}'.format(neighbor[1]))
                    path_edges.append(newEdge)
            dest = prev

        return {'cost': total_length, 'path': path_edges}

    def computeShortestPaths(self, srcIndex, use_heap=False):

        self.source = srcIndex
        t1 = time.time()
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        myNodes = self.network.getNodes()
        myEdges = self.network.getEdges()
        srcNode = myNodes[srcIndex]
        srcNode.changeDistance(0)
        if (use_heap):
            self.myQueue = self.buildHeap(myNodes,srcIndex)
            myNodes[srcIndex].changeDistance(0)
        else:
            self.myQueue = self.buildUnsorted(myNodes)
            myNodes[srcIndex].changeDistance(0)

        while len(self.myQueue) > 0:
          #  print(1)
            if use_heap:
                u = self.deleteMinHeap()
            else:
                u = self.deleteMinUnsorted()
                if(u == None):
                    break
            uID = u.getId()
            myNeighbors = myEdges[uID]
            for edge in myNeighbors:
                nextNode = edge[0]
                neighbor = myNodes[nextNode]
                if neighbor.getDistance() > u.getDistance() + edge[1]:
                    neighbor.changeDistance(u.getDistance() + edge[1])
                    neighbor.changePrev(u)
                    if use_heap:
                        self.decreaseKeyHeap(neighbor.getQueueIndex())
        t2 = time.time()
        return (t2 - t1)


    def buildUnsorted(self, nodes):
        queue = []
        for node in nodes:
            node.changeDistance(float("inf"))
            node.changePrev(None)
            queue.append(node)
        return queue

    #Reset values so I can do multiple in a row
    def buildHeap(self, nodes,src):
        queue = []
        idx = 0
        for node in nodes:
            node.changeDistance(float("inf"))
            node.changePrev(None)
            if node.getId() != src:
                queue.append(node)
                node.setQueueIndex(idx)
            else:
                src = node
                src.setQueueIndex(0)
            idx = idx + 1
        queue.insert(0, src)
        x = "TEST"
        return queue

    #Order doesn't matter, so I don't need this funcion
    #All nodes are added in buildUnsorted()
    def insertUnsorted(self, ):
        pass

    #Since all nodes start out the same distance,
    #I just put the all in the heap randomly
    #I assure the starting node is the root, and I will
    #let descreaseKeyHeaap() determine who is the next root
    #Once the nodes start getting values, the bubble up will
    #correctly place the node in the tree to still have an
    #effective priority queue, so this function is not needed
    def insertHeap(self, ):
        pass

    #Since I am scanning the array in deleteMinHeap(), order doesn't matter.
    #I took advantage of Python's pointer capablities, and this function is not needed
    def decreaseKeyUnsorted(self, queueIndex):
      pass

    def decreaseKeyHeap(self, queueIndex):
        change = True
        curIndex = queueIndex
        while change:
            current = self.myQueue[curIndex]
            parent = curIndex // 2
            if self.myQueue[parent].getDistance() > current.getDistance():
                current.setQueueIndex(parent)
                self.myQueue[parent].setQueueIndex(current)
                self.myQueue[curIndex] = self.myQueue[parent]
                self.myQueue[parent] = current
                curIndex = parent
                continue
            change = False

    def deleteMinUnsorted(self):
        min = None
        length = float("inf")
        index = None
        it = 0
        for stuff in self.myQueue:
            if stuff.getDistance() < length:
                min = stuff
                length = stuff.getDistance()
                index = it
            it += 1
        if index == None:
            return index
        del self.myQueue[index]
        return min

    def deleteMinHeap(self):
        toReturn = self.myQueue[0]
        size = len(self.myQueue)
        last = self.myQueue[size - 1]
        del self.myQueue[size - 1]
        self.myQueue[0] = last
        change = True
        curIndex = 1
        while change:
            child1 = 2 * curIndex
            child2 = child1 + 1
            if self.myQueue[child1-1].getDistance() < last.getDistance():
                last.setQueueIndex(child1-1)
                self.myQueue[child1-1].setQueueIndex(curIndex-1)
                self.myQueue[curIndex-1] = self.myQueue[child1-1]
                self.myQueue[child1-1] = last
                curIndex = child1
                continue
            if self.myQueue[child2-1].getDistance() < last.getDistance():
                last.setQueueIndex(child2-1)
                self.myQueue[curIndex-1] = self.myQueue[child2-1]
                self.myQueue[curIndex - 1] = self.myQueue[child2 - 1]
                self.myQueue[child2-1] = last
                curIndex = child2
                continue
            change = False
        return toReturn






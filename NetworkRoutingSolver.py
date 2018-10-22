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
            self.myQueue = self.buildHeap(myNodes)
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

    def buildHeap(self, nodes):
        queue = []
        for node in nodes:
            if node.getDistance() != 0:
                queue.append(node)
            else:
                src = node
        queue.insert(0, src)
        return queue

    def insertUnsorted(self, ):
        pass

    def insertHeap(self, ):
        pass

    def decreaseKeyUnsorted(self, queueIndex):
        pass

    def decreaseKeyHeap(self, queueIndex):
        pass

    def deleteMinUnsorted(self):
        min = None
        length = float("inf")
        index = None
        it = 0
        for stuff in self.myQueue:
            #what do i do with a tie?
            #print("DISTANCE")
           # print(stuff.getDistance())
          #  print("LENGTH")
          #  print(length)
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
            if self.myQueue[child1].getDistance() < last.getDistance():
                self.myQueue[curIndex] = self.myQueue[child1]
                self.myQueue[child1] = last
                curIndex = child1
                continue
            if self.myQueue[child2].getDistance() < last.getDistance():
                self.myQueue[curIndex] = self.myQueue[child2]
                self.myQueue[child2] = last
                curIndex = child2
                continue
            change = False






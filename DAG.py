import sys


class DAG(object):

    # create empty set for nodes for the DAG
    def __init__(self):
        self.createGraph()

    # prints DAG
    def printDAG(self, graph):
        print(graph)

    # prints the nodes from a list in DAG
    def printNodeList(self, list):
        print(list)

    # creates empty dictionary
    def createGraph(self):
        self.graph = {}

    # add node to DAG (set)
    def addNode(self, node, graph=None):
        if not graph:
            graph = self.graph

        if node in graph:
            return False

        graph[node] = []

    # add edge in the DAG
    def addEdge(self, parent, child, graph=None):
        if not graph:
            graph = self.graph

        if parent in graph and child in graph:
            graph[parent].append(child)
        else:
            print("nodes do not exist")

    # Depth First Search
    def DFS(self, node_list, graph, node):
        if not graph[node]:
            return True
        else:
            for child in graph[node]:
                if child not in node_list:
                    node_list.append(child)
                    if not self.DFS(node_list, graph, child):
                        return self.DFS(node_list, graph, child)
                    node_list.remove(child)
                else:
                    return False
            return True

    # wrapper for Depth First Search
    def Wrapper_DFS(self, graph):
        res = True
        for node in graph:
            if not self.DFS([node], graph, node):
                res = False
                break
        return res

    # wrapper for LCA using Depth First Search
    def Wrapper_LCA(self, graph, node1, node2):
        global nodeList1
        global nodeList2
        nodeList1 = []
        nodeList2 = []

        # storing the node routes for each node into a list
        for node in graph:
            self.LCA_DFS([node], graph, node, 1, node1)
            self.LCA_DFS([node], graph, node, 2, node2)

        leastCount = sys.maxsize
        for a in nodeList1:
            for b in nodeList2:
                count = 0  # +=1 till the node is found
                for ind, node1 in enumerate(reversed(a)):
                    count = ind
                    for node2 in reversed(b):
                        # LCA is the one with the lowest count
                        if node1 == node2 and count < leastCount:
                            LCANode = node2
                            leastCount = count
                            return LCANode
                        count += 1

    # calculates the DFS for an LCA node

    def LCA_DFS(self, nodeList, graph, node, index, endNode):
        # if the node is end node
        if node == endNode:
            # using index for the two routes
            if index == 1:
                nodeList1.append(nodeList[:])
            elif index == 2:
                nodeList2.append(nodeList[:])
            return True

        # if the node is not present in the graph
        if not graph[node]:
            return True

        # in all other cases
        else:
            for child in graph[node]:
                if child not in nodeList:
                    nodeList.append(child)
                    if not self.LCA_DFS(nodeList, graph, child, index, endNode):
                        return self.LCA_DFS(nodeList, graph, child, index, endNode)
                    nodeList.remove(child)
                else:
                    return False
            return True

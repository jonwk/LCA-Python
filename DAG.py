import sys
class DAG(object):

    # prints graph
    def printDAG(self, graph):
       print(graph)

    # prints the nodes from a list from graph
    def printNodeList(self,list):
       print(list)

    # create empty set for nodes for the DAG
    def __init__(self):
        self.createGraph()

    # creates empty dict
    def createGraph(self):
        self.graph = {}

    # add node to set
    def addNode(self, node, graph=None):
        if not graph:
            graph = self.graph

        if node in graph:
            return False

        graph[node] = []

    # add edge to set
    def addEdge(self, ind_node, dep_node, graph=None):
        if not graph:
            graph = self.graph

        # if both nodes exist in the graph
        if ind_node in graph and dep_node in graph:
            graph[ind_node].append(dep_node)
        else:
            raise KeyError("One or both nodes do not exist")

    # function that does DFS
    def DFS(self, node_list, graph, node):
        if not graph[node]:
            return True
        else:
            for child in graph[node]:
                if child not in node_list:
                    node_list.append(child) #Add to list that stores the route
                    if not self.DFS(node_list, graph, child):
                        return False
                    node_list.remove(child)
                else:
                    return False
            return True

    # wrapper for DFS function
    def DFSWrapper(self, graph):
        result = True
        for node in graph:
            if not self.DFS([node], graph, node):
                result = False
                break

        return result

    # wrapper for calculating the LCA using DFS - similar to DFS() but modified code to get LCA to work
    def LCA_DFS_Wrapper(self, graph, nodeA, nodeB):
        global node_A_list
        node_A_list = []
        global node_B_list
        node_B_list = []

        #gets the node routes for each node and stores them into a list
        for node in graph:
            self.LCA_DFS([node], graph, node, 1, nodeA)
            self.LCA_DFS([node], graph, node, 2, nodeB)

        lowest_count = sys.maxsize
        for itemA in node_A_list:
            for itemB in node_B_list:
                count = 0 # count increments per route until node is found
                for index, node1 in enumerate(reversed(itemA)):
                    count = index
                    for node2 in reversed(itemB):
                        if node1 == node2 and count < lowest_count: # LCA is the one with the lowest count
                            LCANode = node2
                            lowest_count = count
                            return LCANode

                        count += 1


    # calculates the DFS for an LCA node
    def LCA_DFS(self, node_list, graph, node, index, end_node):
        if node == end_node:

            # distinguish between the two routes using index
            if index == 1:
                node_A_list.append(node_list[:])
            elif index == 2:
                node_B_list.append(node_list[:])
            return True

        if not graph[node]:
            return True

        else:
            for child in graph[node]:
                if child not in node_list:
                    node_list.append(child) # appends child node to correct node list using the index parameter
                    if not self.LCA_DFS(node_list, graph, child, index, end_node):
                        return False
                    node_list.remove(child)
                else:
                    return False
            return True
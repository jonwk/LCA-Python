class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def findLCA(n1, n2):

    if(n1 > n2):
        temp = n1
        n1 = n2
        n2 = temp

    return findLCAPrivate(root, n1, n2)


def findPath(root, n, path):
    if root is None:
        return False

    path.append(root.data)

    if root.data == n:
        return True

    if((root.left != None and findPath(root.left, n, path)) or (root.right != None and findPath(root.right, n, path))):
        return True

    path.pop()

    return False


def findLCAPrivate(root, n1, n2):
    path1 = []
    path2 = []
    
    if((not findPath(root, n1, path1)) or (not findPath(root, n2, path2))):
        status = ""
        status += ((n1+" is present and ") if len(path1)
                   > 0 else (n1+" is missing"))

        status += ((n2+" is present and ") if len(path2)
                   > 0 else (n2+" is missing"))

        print(status)

        return "Error"

    i = 0
    while(i < len(path1) and i < len(path2)):
        if(path1[i] != path2[i]):
            break
        i += 1

    return path1[i-1]


def print_node(node):
    data = node.data if node.data is not None else "None"
    left_data = "None"
    right_data = "None"

    if(data is not None):
        if(node.left is not None):
            left_data = node.left.data if node.left.data is not None else "None"
        if(node.right is not None):
            right_data = node.right.data if node.right.data is not None else "None"

        print("node data : " + data+"    | node.left : " +
              left_data + "    | node.right : "+right_data)
    else:
        print("node data : " + data)
    return


node1 = root = Node("a")
node2 = root.left = Node("b")
node3 = root.right = Node("c")
node4 = node2.left = Node("d")
node5 = node2.right = Node("e")

node6 = node3.left = Node("f")
node7 = node3.right = Node("g")

node8 = node4.left = Node("h")
node9 = node5.right = Node("i")

node10 = node6.left = Node("j")
node11 = node7.right = Node("k")

print("LCA(d, e) is "+findLCA("d", "e"))
print("LCA(d, f) is "+findLCA("d", "f"))
print("LCA(c, d) is "+findLCA("c", "d"))
print("LCA(b, d) is "+findLCA("b", "d"))
print("LCA(h, i) is "+findLCA("h", "i"))
print("LCA(j, l) is "+findLCA("j", "l"))
print("LCA(j, k) is "+findLCA("j", "k"))
print("LCA(h, d) is "+findLCA("h", "d"))
print("LCA(l, d) is "+findLCA("l", "d"))

import Options

const RED:bool = true
const Black:bool = false

type
    Node* = ref object of RootObj
        key: string
        value: int
        N: int
        color: bool #father node chain to it color
        left: Node
        right: Node 

proc isRed*(node:Node): bool =
    if node == nil:
        return false
    return node.color == RED

proc size_node*(node:Node): int = 
    if node == nil:
        return 0
    else:
        return node.N

# right red chain rotate to left
proc rotateLeft*(node:var Node): Node =
    var x: Node = node.right

    node.right = x.left 
    x.left = node 
    x.color = node.color
    node.color = RED
    x.N = node.N
    node.N = 1 + size_node(node.left) + size_node(node.right)
    return x

# left red chain rotate to right
proc rotateRight*(node:var Node): Node =
    var x: Node = node.left

    node.left = x.right
    x.right = node
    x.color = node.color
    x.N = node.N
    node.N = 1 + size_node(node.left) + size_node(node.right)
    return x

# turn left right red chain to black and self color to red
proc flipColors(node:Node) =
    node.color = RED
    node.left.color = Black
    node.right.color = Black

type
    RedBlackBST* = ref object of RootObj
        root:Node

proc size*(rb:RedBlackBST): int =
    return size_node(rb.root)

proc put_node*(node:var Node, key:string, value:int): Node =

    if node == nil:
        return Node(key:key, value:value, N:1, color:RED, left:nil, right:nil)

    if key > node.key:
        node.right = put_node(node.right, key, value)
    
    elif key < node.key:
        node.left = put_node(node.left, key, value)
    else:
        node.value = value
    
    # rotate red chain
    if isRed(node.right) and  not isRed(node.left):
        node = rotateLeft(node)
    
    elif isRed(node.right) and isred(node.left.right):
        node = rotateRight(node)
    
    elif isRed(node.left) and isRed(node.right):
        flipColors(node)
    node.N = size_node(node.left) + size_node(node.right) + 1
    
    result = node
    return result

proc put(rb:RedBlackBST,key:string, value:int) =
    rb.root = put_node(rb.root, key, value)
    rb.root.color = Black

proc get_node*(node:Node, key:string): Option[int] =
    if node == nil:
        return none(int)
    if key < node.key:
        return get_node(node.left, key)
    elif key > node.key:
        return get_node(node.right, key)
    else:
        return some(node.value)

proc get*(rb:RedBlackBST,key:string): Option[int] = 
    return get_node(rb.root, key)

proc main() = 
    var 
        bst:RedBlackBST = RedBlackBST(root:nil)
    bst.put("a", 1)
    echo bst.get("a").get()
    bst.put("b", 2)
    echo bst.size()
    bst.put("a", 3)
    echo bst.get("a")
    echo bst.size()

main()

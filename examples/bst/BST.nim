import options


type
    BST* = ref object of RootObj
        root:Node

    Node = ref object of RootObj
        key:string
        value:int
        left:Node 
        right:Node 
        N:int

proc size_node(node:Node): int = 
    if node == nil:
        return 0
    else:
        return node.N
    
proc size*(bst:BST):int = 
    return size_node(bst.root)

proc get_node(node:Node, key:string): Option[int] = 
    if node == nil:
        return none(int)
    if key < node.key:
        return get_node(node.left, key)
    elif key > node.key:
        return get_node(node.right, key)
    else:
        return some(node.value)

proc get*(bst:BST, key:string): Option[int] =
    return get_node(bst.root, key)

proc put_node(node:Node, key:string, value:int):Node = 
    if node == nil:
        return Node(key:key, value:value, left:nil, right:nil, N:1)
    
    if key > node.key:
        node.right = put_node(node.right, key, value)
    elif key < node.key:
        node.left = put_node(node.left, key, value)
    else:
        node.value = value
    node.N = size_node(node.left) + size_node(node.right) + 1
    return node

proc put*(bst:BST, key:string, value:int) =
    bst.root = put_node(bst.root, key, value)




proc main() = 
    var 
        bst:BST = BST(root:nil)
    bst.put("a", 1)
    echo bst.get("a").get()
    bst.put("b", 2)
    echo bst.size()
    bst.put("a", 3)
    echo bst.get("a")
    echo bst.size()

main()
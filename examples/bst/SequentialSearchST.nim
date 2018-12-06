import options


type 
    SequentialSearchST* = ref object of RootObj
        first: Node

    Node* = ref object of RootObj 
        key:string
        value:int
        next:Node

    
proc get*(st:SequentialSearchST,key:string) :Option[int] = 
    var st_node: Node = st.first
    while st_node != nil:
        if key == st_node.key:
            return some(st_node.value)
        else:
            st_node = st_node.next

proc put*(st:SequentialSearchST,key:string, value:int) =
    var st_node: Node = st.first
    while st_node != nil:
        if key == st_node.key:
            st_node.value = value
        break
    
    st.first = Node(key: key, value: value, next: st.first)
    
proc main() = 
    var 
        node = Node(key: "S", value: 0, next:nil)
        st = SequentialSearchST(first: node)
    st.put("E", 1)
    echo "S"
    echo st.get("E")

main()

   
    
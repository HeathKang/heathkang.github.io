import options


type 
    BinarySearchST* = ref object of RootObj
        keys: seq[string]
        vals: seq[int]
        N: int

proc size*(bt: BinarySearchST): int = 
    return bt.N

proc rank*(bt: BinarySearchST, key: string): int = 
    var
        lo = 0
        hi = bt.N - 1
        mid = 0

    while lo <= hi:
        mid = lo + (hi - lo) div 2
        if key < bt.keys[mid]:
            hi = mid - 1
        elif key > bt.keys[mid]:
            lo = mid + 1
        else:
            return mid
    return lo

proc get*(bt: BinarySearchST, key: string): Option[int] = 
    var i:int = bt.rank(key)
    if i < bt.N and bt.keys[i] == key:
        return some(bt.vals[i])
    else:
        return none(int)

proc put*(bt: BinarySearchST, key: string, val:int) = 
    var i:int = bt.rank(key)
    # key is already in keys
    if i < bt.N and bt.keys[i] == key:
        bt.vals[i] = val
        return
    # add key and val in proper location
    var j:int = bt.N
    # add keys and vals length
    bt.keys.add("")
    bt.vals.add(0)
    while j > i:
        bt.keys[j] = bt.keys[j - 1]
        bt.vals[j] = bt.vals[j - 1]
        j = j - 1

    bt.keys[i] = key
    bt.vals[i] = val
    bt.N = bt.N + 1


proc main() =
    var 
        bt = BinarySearchST(keys: @["a"], vals: @[1], N:1)

    echo bt.get("a")
    bt.put("b", 2)
    bt.put("c", 3)
    echo bt.get("c").get()
    echo bt.get("e")

main()

        
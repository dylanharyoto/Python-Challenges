def hst(string):
    store = {"a":0, "e":0, "i":0, "o":0, "u":0}
    for char in string:
        char = char.lower()
        if char in ["a", "i", "u", "e", "o"]:
            store[char] += 1
    max = 0
    for val in store.values():
        if val > max:
            max = val
    for i in range(max):
        for val in store.values():
            if val < max-i:
                print("   ", end="")
            else:
                print("  *", end="")
        print("\n", end="")
    print("=================\n  a  e  i  o  u  ")

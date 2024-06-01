def pcp():
    store = {}
    score = ""
    while True:
        score = input()
        if score == "-1":
            break
        score = score.split(" ")
        performance = int(score[0]) + int(score[1]) + int(score[2])
        result = performance / float(score[3])
        if result not in store:
            store[result] = score
    hppr = max(store.keys())
    hppr_score = sum([int(x) for x in store[hppr][:3]])
    hppr_value = " ".join(store[hppr])
    print(hppr_value)
    del store[hppr]
    for value in store.values():
        score = sum([int(x) for x in value[:3]])
        if score > hppr_score:
            print(" ".join(value))

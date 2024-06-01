def mn():
    # (514,324,764,42,120,836,527,935,83,155,453,648,14)
    # (542,914,436,973,605,813,678,237,285,296,372)
    # (373,520,111,417,954,572,796,897,469,281,931,925,697,90)
    X = eval(input())
    sum = 0
    Xmin, Xmax = X[0], X[1]
    for i in range(len(X)):
        sum += X[i]
        if X[i] < Xmin:
            Xmin = X[i]
        if X[i] > Xmax:
            Xmax = X[i]
    Xmean = sum / len(X)
    Xn = []
    for x in X:
        Xn.append(f'{(x - Xmean) / (Xmax - Xmin):0.3f}')
    print(",".join(Xn))

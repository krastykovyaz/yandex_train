# [(0.5, 1),(0.2, 0)]

def get_threshold(vector)->int:
    svector = sorted(vector)
    accuracy = []
    TP = 0
    TN = 0
    print(svector)
    for pred, label in svector:
        thresh = svector[0][0]
        if thresh <= pred:
            if label == 1:
                TP += 1
        else:
            if label == 0:
                TN += 1
    accuracy = TP + TN
    max_acc = accuracy
    res = svector[0][0]
    for i in range(1,len(svector)):
        if svector[i-1][1] == 1:
            accuracy -= 1
        else:
            accuracy += 1
        if max_acc < accuracy:
            max_acc = accuracy
            res = svector[i][0]
    return res


if __name__=='__main__':
    inpt = [(0.2,0),(0.3,1),(0.4,0),(0.4,1),(0.5,1)]
    print(get_threshold(inpt))

            

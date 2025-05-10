def compare(d,a):#辞書の1単語とアナグラムのどちらが先か（0アナグラム先:，1:アナグラム後，2:一致）
    if len(a)>len(d):
        r = 1
        range_ = len(d)
    elif len(a)<len(d):
        r = 0
        range_ = len(a)
    else:
        r = 2
        range_ = len(a)


    for i in range(range_):
        if a[i] < d[i]:
            return 0
        elif a[i] > d[i]:
            return 1
    
    return r


def binary(d,a):#二分探索
    left = 0
    right = len(d)
    p = int((left+right)/2)

    while(left<=right):
        q = compare(d[p][0],a[0])
        if q ==0:
            right = p-1
        elif q == 1:
            left = p+1
        else:
            return d[p][1] #一致した

        
        p = int((left+right)/2)

    return "****Error****"

def main():
    #辞書とアナグラムのソート
    dictionary = []
    with open("words.txt") as f:
        for line in f:
            w = line.rstrip()
            dictionary.append([sorted(w),w])
    newdictionary = sorted(dictionary)
  
    with open("01_anagram_01_TestCase.txt") as f:
        for line in f:
            a = line.rstrip()
            anagram=[sorted(a),a]
            print(binary(newdictionary,anagram))

main()

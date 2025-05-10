def compare(d,a):#辞書の1単語とアナグラムのどちらが先か（-1アナグラム先:，1:アナグラム後，0:一致）
    if len(a)>len(d):
        r = 1
        range_ = len(d)
    elif len(a)<len(d):
        r = -1
        range_ = len(a)
    else:
        r = 0
        range_ = len(a)


    for i in range(range_):
        if a[i] < d[i]:
            return -1
        elif a[i] > d[i]:
            return 1
    
    return r


def binary(d,a):#二分探索
    left = 0
    right = len(d)
    mid = int((left+right)/2)
    ans = []

    while(left <=right):
        q = compare(d[mid][0],a[0])
        if q == -1:
            right = mid-1
        elif q == 1:
            left = mid+1
        else:
            ans.append(d[mid][1])
            for i in range(mid-2):#さかのぼる
                if compare(d[mid-1-i][0],a[0]) == 0:
                    ans.append(d[mid-1-i][1])
                else:
                    break
            for i in range(len(d)-mid-1):
                if compare(d[mid+1+i][0],a[0]) == 0:
                    ans.append(d[mid+1+i][1])
                else:
                    break
            return sorted(ans)
        
        mid = int((left+right)/2)

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

alphabet_score = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
                  [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]]

def count_alphabet(w):
    w_count = []
    w_list = list(w)
    for i in range(len(alphabet_score[0])):
        w_count.append(w_list.count(alphabet_score[0][i]))
    return w_count

def compare(d,a):
    score = 0
    for i in range(len(alphabet_score[0])):
        if a[0][i]<d[0][i]:
            return -100 #作れない
        else: score = score+ d[0][i]*alphabet_score[1][i]
    return score

def search_max(dictionary,anagram):
    max_score = 0
    max_i = 0

    for i in range(len(dictionary)):
        if compare(dictionary[i],anagram)>max_score:
            #print("___",dictionary[i][1])
            max_i = i
            max_score = compare(dictionary[i],anagram)
        
    return dictionary[max_i][1],max_score

    
def main():
    #単語に使われている文字数をカウント
    dictionary = []
    with open("words.txt") as f:
        for line in f:
            w = line.rstrip()
            dictionary.append([count_alphabet(w),w])

    with open("small.txt") as f:
        with open("small_answer.txt",mode='w') as g:
            for line in f:
                a = line.rstrip()
                anagram = [count_alphabet(a),a]

                g.write(search_max(dictionary,anagram)[0])
                g.write('\n')

    with open("medium.txt") as f:
        with open("medium_answer.txt",mode='w') as g:
            for line in f:
                a = line.rstrip()
                anagram = [count_alphabet(a),a]

                g.write(search_max(dictionary,anagram)[0])
                g.write('\n')

    with open("large.txt") as f:
        with open("large_answer.txt",mode='w') as g:
            for line in f:
                a = line.rstrip()
                anagram = [count_alphabet(a),a]

                g.write(search_max(dictionary,anagram)[0])
                g.write('\n')

main()

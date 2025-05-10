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
    return d[2]

def search_max(dictionary,anagram):

    for i in range(len(dictionary)):
        if compare(dictionary[i],anagram)>0:
            return dictionary[i][1]
    return "****Error****"

def calc_score(word_count):
    score = 0
    for i in range(len(alphabet_score[1])):
        score += word_count[i]*alphabet_score[1][i]
    return score


    
def main():
    #単語に使われている文字数をカウント
    old_dictionary = []
    with open("words.txt") as f:
        for line in f:
            w = line.rstrip()
            w_list = count_alphabet(w)
            old_dictionary.append([w_list,w,calc_score(w_list)])
    dictionary = sorted(old_dictionary, key = lambda x: x[2],reverse=True)
        
    with open("small.txt") as f:
        with open("small_answer.txt",mode='w') as g:
            for line in f:
                a = line.rstrip()
                anagram = [count_alphabet(a),a]

                g.write(search_max(dictionary,anagram))
                g.write('\n')

    with open("medium.txt") as f:
        with open("medium_answer.txt",mode='w') as g:
            for line in f:
                a = line.rstrip()
                anagram = [count_alphabet(a),a]

                g.write(search_max(dictionary,anagram))
                g.write('\n')

    with open("large.txt") as f:
        with open("large_answer.txt",mode='w') as g:
            for line in f:
                a = line.rstrip()
                anagram = [count_alphabet(a),a]

                g.write(search_max(dictionary,anagram))
                g.write('\n')

main()
"""
Exercise 2:
    *. Lexicographical order is often known as alphabetical
    order when dealing with strings. A string is greater than
    another string if it comes later in a lexicographically sorted list.
    Given a word, create a new word by swapping some or all of its 
    characters. This new word must meet two criteria:
        ● It must be greater than the original word
        ● It must be the smallest word that meets the first condition

    *. Example w = abcd
    The next largest word is abdc.

    *. Create the function bigger_Is_greater and return the new string
    meeting the criteria. If it is not possible, return no answer.

    *. Function Description
    Function has the following parameter(s):
        ● string w: a word
    Returns
    	- 	string: the smallest lexicographically higher string 
        possible or no answer

    *. Input Format
    The first line of input contains T, the number of test cases. 
    Each of the next T lines contains w.

    *. Constraints
        ● 1 ≤ T ≤ 105
        ● 1 ≤ length of w ≤ 100
        ● w will contain only letters in the range ascii[a...z]

    *. Sample Input:
    5 ab bb hefg dhck dkhc

    Sample Output
        ba 
        no answer
        hegf
        dhkc
        hcdk
"""
def bigger_Is_greater(w):

    w = list(w)
    i = len(w)-1
    while i > 0 and w[i-1] >= w[i]:
        i -= 1

    if i <= 0:
        return 'no answer'

    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1
    
    w[i-1], w[j] = w[j], w[i-1]
    w[i:] = w[len(w)-1:i-1:-1]

    return ''.join(w)


T = int(input("Enter T\n"))
my_ascii = [_ for _ in range(97,123)]
if(T > 0 and T <= pow(10,5)):
    count_loop = 0
    my_words = []
    while True:
        count_loop += 1
        
        W = input()
        if(len(W) <= 100):
            flag = True
            for letter in W:
                if(ord(letter) not in my_ascii):
                    flag = False
                    print("symbols not from a to z detected!")
                    break;

            if(flag):
                my_words.append(W)
        else:
            print("Error: Length of W is too high!")
        
        if count_loop >= T:
            break;
    
    for w in my_words:
        print(bigger_Is_greater(w))

else:
    print("Error: N is too ambitious!")\


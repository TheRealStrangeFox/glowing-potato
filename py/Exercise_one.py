"""
Exercise 1:
    *. You are given words. Some words may repeat. 
    For each word, output its number of occurrences. 
    The output order should correspond with the input 
    order of appearance of the word. See the sample 
    input/output for clarification.

    *.Note: Each input line ends with a "\n" character.

    *.Constraints:
    1 ≤ n ≤ 10^5
        The sum of the lengths of all the words do not 
    exceed 10^6 All the words are composed of 
    lowercase English letters only.

    *.Input Format:
    The first line contains the integer, n.
    The next n lines each contain a word.

    *.Output Format
    Output 2 lines.
    On the first line, output the number of distinct 
    words from the input.
    On the second line, output the number of occurrences for 
    each distinct word according to their appearance in the input.

    *.Sample Input:
    4 
    bcdef
    abcdefg
    bcde
    bcdef

    *.Sample Output
    3
    2 1 1

    *.Explanation
    There are 3  distinct words. Here, "bcdef" appears 
    twice in the input at the first and last positions. 
    The other words appear once each. The order of the 
    first appearances are "bcdef", "abcdefg" and "bcde" 
    which corresponds to the output.
"""
sample_input_size = 0
input_dict = {};
n = int(input())
if(n > 0 and n <= pow(10,5)):
    count_loop = 0
    while n:
        count_loop += 1
        input_variable = input()
        for letter in input_variable:
            if ord(letter) not in range(97,123):
                print("symbols not from a to z detected!")
                break;
        input_variable = input_variable.strip('\\n')
        sample_input_size += len(input_variable)

        if sample_input_size >= pow(10,6):
            print("Error: The sum of the lengths" 
                + "of all the words exceeded 10^6! Please try again!\n")
        elif not input_variable.isnumeric(): 
            if input_variable in input_dict.keys():
                input_dict[input_variable] += 1
            else:
                input_dict[input_variable] = 1

        if count_loop >= n:
            break;
            
    print("\n" + str(len(input_dict.keys())))
    for i in input_dict.values():
        print(i,end=' ')
else:
    print("Error: N is too ambitious!")


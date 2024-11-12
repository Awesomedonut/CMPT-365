def lzw_coding(input, dict):
    s = input[0]
    result = []

    for i in range(1, len(input)):  # while not EOF
        c = input[i]
        if (s+c) in dict:
            s += c
        else:
            result.append(dict[s])
            print("output " + str(dict[s])) # output code for s
            dict[s+c] = len(dict)  # new entry to the dictionary
            s = c
    result.append(dict[s])  # output code for s
    print("output " + str(dict[s]))

    print("final output is " + str(result))
    print("final dict is " + str(dict))


initial_dict = {'A': 0, 'B': 1}
lzw_coding("AABABAB", initial_dict)
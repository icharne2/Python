def find_pattern_method_1(text, pattern):
    count = 0
    len_text = len(text)
    len_pattern = len(pattern)

    for i in range(len_text - len_pattern + 1):
        for x in range(len_pattern):
            if text[i + x] != pattern[x]:
                break
        else:
            print("Pattern found:", pattern, "at position", i)
            count += 1

    if count != 0:
        print("The pattern occurred:", count, "times")
    else:
        print("The pattern is not present in the text")

find_pattern_method_1("matematyka", "mat")

def find_pattern_method_2(text, pattern):
    count = 0
    len_text = len(text)
    len_pattern = len(pattern)

    for i in range(len_text - len_pattern + 1):
        if text[i:i + len_pattern] == pattern:
            print("Pattern found:", pattern, "at position", i)
            count += 1

    if count != 0:
        print("The pattern occurred:", count, "times")
    else:
        print("The pattern is not present in the text")

find_pattern_method_2("matematyka", "mat")

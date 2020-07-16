ignore = (":", ";", ",", ".", "-", "+", "=", "/", "\\", "|",
               "[", "]", "{", "}", "(", ")", "*", "^", "&", "\"")


def word_count(s):
    counts = {}

    # convert to lower case
    # split words into list
    for char in ignore:
        s = s.replace(char, "")
    s = s.lower().split()

    if len(s) == 1 and s[0] == "":
        return {}

    for word in s:
        if word in counts:
            counts[word.lower()] += 1
        else:
            counts[word.lower()] = 1
    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))

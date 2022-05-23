'''input is a word or sentence(string)
output is the string'''

def reverse(word):
    return word[::-1]

def reverse_sentence(sentence):
    word = sentence.split(" ")
    word = [i[::-1] for i in word]
    return " ".join(word)

def test():
    a = "appleisgood"
    b = "i have a treee is in the bed"
    a_t = "doogsielppa"
    b_t = "i evah a eeert si ni eht deb"
    if(reverse(a) == a_t and reverse_sentence(b) == b_t): return True

# word = reverse("1234")
# print(word)
# sentence = reverse_sentence("i have apple")
# print(sentence)

# test
print(test())
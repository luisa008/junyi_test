def reverse(word):
    return word[::-1]

def reverse_sentence(sentence):
    word = sentence.split(" ")
    word = [i[::-1] for i in word]
    return " ".join(word)

word = reverse("1234")
print(word)
sentence = reverse_sentence("i have apple")
print(sentence)
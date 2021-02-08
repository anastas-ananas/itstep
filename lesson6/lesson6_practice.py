text = "Sentence one, sentence one. Sentence two. Sentence three: sentence three."
count = 0
print('total sentences:    ', text.count('.'))
for symbols in range (0, len (text)):
    if text[symbols] in ('!', ",", ";", ".", "-", "?", ":"):
        count = count + 1
print ("Total number of punctuation characters exists in SENTENCES: ")
print (count)
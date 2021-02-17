from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

text = "The quick brown fox jumped over the lazy dog"
tokens = text.split()
print(tokens)

text = "The quick brown fox, and an Oxford comma"
tokens = text.split()
print(tokens)


from nltk.tokenize import word_tokenize
text = "The quick brown fox, and an Oxford comma"
tokens = word_tokenize(text)
print(tokens)


from nltk.tokenize import word_tokenize
text = "Tweet about #NLProc @ABCD :)"
tokens = word_tokenize(text)
print(tokens)

from nltk.tokenize import TweetTokenizer
text = "Tweet about #NLProc @ABCD :)"
tokenizer = TweetTokenizer()
tokens = tokenizer.tokenize(text)
print(tokens)

from nltk.tokenize import TweetTokenizer
text = "Tweet about #NLProc @ABCD :)"
tokenizer = TweetTokenizer(strip_handles=True)
tokens = tokenizer.tokenize(text)
print(tokens)

from nltk.tokenize import word_tokenize
text = "How about currencies (like £100,000.00) and dates (like 19th September)"
tokens = word_tokenize(text)
print(tokens)


from nltk.stem import PorterStemmer

s = PorterStemmer()
print(s.stem('Having'))
print(s.stem('Have'))
print(s.stem('Had'))

print(s.stem('Fishing'))
print(s.stem('Fish'))
print(s.stem('Fisher'))
print(s.stem('Fishes'))
print(s.stem('Fished'))

print(s.stem('European'))
print(s.stem('Europe'))

print(s.stem('policy'))
print(s.stem('police'))

print(s.stem('matrix'))
print(s.stem('matrices'))

print(s.stem('automation'))
print(s.stem('automatic'))
print(s.stem('automate'))
print(s.stem('automat'))
print(s.stem('was'))
print(s.stem('saw'))

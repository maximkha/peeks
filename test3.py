from Peeks import Peekstr

s = "I am a string" #"I am a string"

peeked = Peekstr(s)
for c in peeked:
    if c == "": break #peeked does not throw a stop iterator!!!
    if peeked.peek(4) == "am a":
        print("I found the substring!")
        print(f"{peeked.Position}")
        break

peeked = Peekstr(s)
for c in peeked:
    if c == "": break #peeked does not throw a stop iterator!!!
    print(c)
    if peeked.peek(1) == "a":
        peeked.consume(1) #skip the next character if it's an 'a'
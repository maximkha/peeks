from Peeks import Peekstr
from Peeks import Peeks

#s = "I am a string" #"I am a string"
s = "1234 I am a string"

peeked = Peekstr(s)
print("peek")
print(peeked.peek(1, 0))
print(peeked.peek(2, 0))
print(peeked.peek(1, 2))
print(peeked.peek(2, 0))
print(peeked.peek(1, 0))

print("consume")
print(peeked.consume(1))

print("peek")
print(peeked.peek(1, 0))
print(peeked.peek(2, 0))
print(peeked.peek(1, 2))
print(peeked.peek(2, 0))
print(peeked.peek(1, 0))

# really cool demo of compact search
while True:
    if peeked.peek(4) == "am a":
        print("found it")
        print(f"{peeked.Position=}")
        print(f"{s[peeked.Position:]=}")
        break
    elif peeked.consume(1) == "":
        print("didn't find it!")
        break

# demo of how the buffer actually works
# while True:
#     if peeked.peek(4) == "am a":
#         print("found it")
#         break
#     print(f"{peeked.Buffer=}")
#     if peeked.consume(1) == "":
#         print("didn't find it!")
#         break
#     print(f"{peeked.Buffer=}")
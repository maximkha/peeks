from Peeks import Peeks

s = "I am a string" #"I am a string"

peeked = Peeks(s)
# print("peek")
# print(peeked.peek(1, 0))
# print(peeked.peek(2, 0))
# print(peeked.peek(1, 2))
# print(peeked.peek(2, 0))
# print(peeked.peek(1, 0))

# print("consume")
# print(peeked.consume(1))

# print("peek")
# print(peeked.peek(1, 0))
# print(peeked.peek(2, 0))
# print(peeked.peek(1, 2))
# print(peeked.peek(2, 0))
# print(peeked.peek(1, 0))

while True:
    if peeked.peek(4) == list("am a"):
        print("found it")
        break
    elif peeked.consume(1) == [None]:
        break
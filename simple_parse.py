from enum import Enum
from Peeks import Peekstr

operators = list("+-*/")
numbers = list("1234567890")

IN_STR = "(1*6)+7+4"

class ParseState(Enum):
    NORMAL = 0
    COLLECT = 1

def consumenumber(peek: Peekstr):
    decimal = False
    strbuf = ""
    while True:
        if peek.peek(1) in numbers:
            strbuf += peek.consume(1)
        elif peek.peek(1) == ".":
            if decimal: raise ValueError("Double decimal?")
            else: decimal = True
            strbuf += "."
        else:
            return float(strbuf)

def parsemath(s):
    peeked = Peekstr(s)
    mode = ParseState.NORMAL
    values = []
    current_operator = ""
    nopen = 0
    pbuff = ""
    while True:
        if peeked.peek(1) == "(":
            mode = ParseState.COLLECT
            peeked.consume(1)
            nopen += 1
        elif peeked.peek(1) == ")":
            nopen -= 1
            peeked.consume(1)
            if nopen == 0:
                parsemath(pbuff)
                mode = ParseState.COLLECT
            elif nopen < 0:
                raise ValueError("forgot ( ?")
        elif mode == ParseState.COLLECT:
            pbuff += peeked.consume(1)
        elif peeked.peek(1) == "-" and peeked.peek(2) in numbers:
            #unary minus
            peeked.consume(1)
            values.append(-consumenumber(peeked))
        elif peeked.peek(1) in numbers:
            values.append(consumenumber(peeked))
        elif peeked.peek(1) in operators:
            current_operator = peeked.consume(1)
        elif peeked.peek(1) == "":
            return values[0]

print(parsemath(IN_STR))
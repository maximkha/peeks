from Peeks import Peekstr

NUMBERS = list("1234567890")
OPERATORS = list("+-*/")

def applyop(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        raise ValueError(f"Invalid operator '{op}'")

def parse_math(s):
    print(f"parsing {s=}")
    ps = Peekstr(s)
    saw_num = False
    want_rhs = False

    value = 0
    cur_op = "+"
    while True:
        if ps.peek(1) == "(":
            ps.consume(1)
            nopen = 1
            buffer = ""
            while True:
                val = ps.consume(1)
                if val == "(":
                    nopen += 1
                    buffer += val
                elif val == ")":
                    nopen -= 1
                    if nopen == 0:
                        value = applyop(value, parse_math(buffer), cur_op)
                        want_rhs = False
                        break
                    else:
                        buffer += val
                else:
                    buffer += val
        elif ps.peek(1) in OPERATORS and saw_num:
            cur_op = ps.consume(1)
            want_rhs = True
        elif ps.peek(1) in NUMBERS or ps.peek(1)=="-":
            buffer = ps.consume(1) # consume first number or minus (this is to make the next part easier)
            buffer += ps.consume_until(lambda x: x not in NUMBERS and x != ".", False)
            print(f"{buffer=}")
            value = applyop(value, float(buffer), cur_op)
            saw_num = True #parse
            want_rhs = False
        elif ps.peek(1) == "":
            if want_rhs: raise ValueError("ended too early")
            return value
        else:
            raise ValueError(f"unexpected character {ps.peek(1)=}")


# parse_math("-2.34512+3")
# parse_math("-+")
print(parse_math("-2.34512+3."))
# print(parse_math("((2))"))
#print(parse_math("2"))
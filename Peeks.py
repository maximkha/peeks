from typing import Iterable, Iterator, List, Sequence, TypeVar, Callable, Union

T = TypeVar('T')

class Peeks:
    def __init__(self, source: Iterable[T]) -> None:
        self.Iterator: Iterator[T] = iter(source)
        self.Buffer: List[T] = []
        self.Position: int = 0

    def __iter__(self) -> Iterator[T]:
        return self
    
    def __next__(self) -> T:
        return self.consume(1)
    
    def consume(self, n: int) -> List[T]:
        retbuff: List[T] = []
        for _ in range(n):
            if len(self.Buffer) > 0:
                retbuff.append(self.Buffer.pop(0))
                self.Position += 1
            else: 
                val = None
                try:
                    val = next(self.Iterator)
                    self.Position += 1
                except StopIteration:
                    return retbuff
                retbuff.append(val)
        return retbuff

    def consume_until(self, condition: Callable[[T], bool], consume_last: bool = False) -> List[T]:
        retbuff = []
        while True:
            if condition(self.peek(1)):
                if consume_last:
                    retbuff.extend(self.consume(1))
                return retbuff

            consumed = self.consume(1)
            retbuff.extend(consumed)
            # if len(consumed) == 0 or None in consumed:
            #     return retbuff
            if len(consumed) == 0: return retbuff
    
    def peek(self, n: int, pos: int=0) -> List[T]:
        retbuff: List[T] = []
        for i in range(n + pos):
            if len(self.Buffer) - i > 0:
                retbuff.append(self.Buffer[i])
                continue

            val = None
            try:
                val = next(self.Iterator)
            except StopIteration:
                return retbuff
            self.Buffer.append(val)
            if i >= pos: retbuff.append(val)
        return retbuff

    def has(self, value: Sequence, pos: int=0) -> bool:
        return self.peek(len(value), pos) == value
    
    # def consume_has(self, value: Sequence, step: int=1) -> List[T]:
    #     retbuff = []
    #     while True:
    #         if self.has(value):
    #             retbuff.extend(self.consume(len(value)))
    #             return retbuff

    #         consumed = self.consume(step)
    #         retbuff.extend(consumed)
    #         if len(consumed) == 0 or None in consumed:
    #             return retbuff
    
    def consume_multiple(self, values: Sequence[Sequence], consume_last: bool = False, step: int=1) -> List[T]:
        retbuff = []
        while True:
            for value in values:
                if self.has(value):
                    if consume_last:
                        retbuff.extend(self.consume(len(value)))
                    return retbuff
            
            consumed = self.consume(step)
            retbuff.extend(consumed)
            if len(consumed) == 0 or None in consumed:
                return retbuff

class Peekstr(Peeks):
    def __init__(self, source: Iterable[str]) -> None:
        Peeks.__init__(self, source)
    
    def __iter__(self) -> Iterator[str]:
        return Peeks.__iter__(self)

    def __next__(self) -> str:
        return Peeks.__next__(self)

    def consume_until(self, condition: Union[List[str], str, Callable[[str], bool]], consume_last: bool = False) -> str:
        res = []
        if isinstance(condition, list):
            if all(map(lambda x: len(x) <= 1, condition)):
                res = Peeks.consume_until(self, lambda x: x in condition, consume_last)
            else:
                res = Peeks.consume_multiple(self, condition, consume_last)
        elif isinstance(condition, str):
            if len(condition) <= 1:
                res = Peeks.consume_until(self, lambda x: x == condition, consume_last)
            else:
                res = Peeks.consume_multiple(self, [condition], consume_last)
        else:
            res = Peeks.consume_until(self, condition, consume_last)
        
        return "".join(filter(None, res))

    def consume(self, n) -> str:
        return "".join(filter(None, Peeks.consume(self, n)))
    
    def peek(self, n, pos=0) -> str:
        return "".join(filter(None, Peeks.peek(self, n, pos)))
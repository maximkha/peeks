from typing import Iterable, Iterator, List, TypeVar, cast

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
    
    def consume(self, n) -> List[T]:
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
                except StopIteration: pass
                retbuff.append(val)
        return retbuff
    
    def peek(self, n, pos=0) -> List[T]:
        retbuff: List[T] = []
        for i in range(n + pos):
            if len(self.Buffer) - i > 0:
                retbuff.append(self.Buffer[i])
                continue

            val = None
            try:
                val = next(self.Iterator)
            except StopIteration: pass
            self.Buffer.append(val)
            if i >= pos: retbuff.append(val)
        return retbuff

class Peekstr(Peeks):
    def __init__(self, source: Iterable[str]) -> None:
        Peeks.__init__(self, source)
    
    def consume(self, n) -> str:
        return "".join(filter(None, Peeks.consume(self, n)))
    
    def peek(self, n, pos=0) -> str:
        return "".join(filter(None, Peeks.peek(self, n, pos)))
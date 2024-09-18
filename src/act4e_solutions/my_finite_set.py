from typing import Any, TypeVar, cast, Collection, Iterator, List

import act4e_interfaces as I

E = TypeVar("E")

class MyFiniteSet(I.FiniteSet[E]):
    _elements: List[E]
    def __init__(self, elements: Collection[E]):
        self._elements = list(elements)
    def size(self) -> int:
        return len(self._elements)
    def contains(self, x: E) -> bool: 
        for y in self._elements:
            if self.equal(x, y): 
                return True
        return False
    def elements(self) -> Iterator[E]: 
        for _ in self._elements:
            yield _
    def save(self, h: I.IOHelper, x: E) -> I.ConcreteRepr:
        return cast(I.ConcreteRepr, x)  
    def load(self, h: I.IOHelper, o: I.ConcreteRepr) -> E: 
        return cast(E, o)
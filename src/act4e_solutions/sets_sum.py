from typing import Any, Sequence, TypeVar, Tuple, List, cast, Iterator

import act4e_interfaces as I

X = TypeVar("X")
C = TypeVar("C")
E = TypeVar("E")


class MyFiniteSetDisjointUnion(I.FiniteSetDisjointUnion[C,List[C]]):
    _components: List[I.FiniteSet[C]]
    def __init__(self, components: Sequence[I.FiniteSet[C]]):
        self._components = list(components)

    def components(self) -> Sequence[I.FiniteSet[C]]:
        return self._components
    
    def contains(self, x: List[C]) -> bool:
        if not isinstance(x, tuple) or len(x)!=2:
            return False
        i, e = x
        if i<0 or i>=len(self._components):
            return False
        comp = self._components[i]
        return comp.contains(e)

        

    def size(self) -> int:
        ans = 1
        for c in self._components:
            ans *= c.size()
        return ans
    
    def elements(self) -> Iterator[List[C]]:
        from itertools import product
        # Generate Cartesian product of elements from all components
        for combination in product(*(comp.elements() for comp in self._components)):
            yield tuple((i, elem) for i, elem in enumerate(combination))

    
    
    def pack(self, i: int, e: C) -> List[C]:
        if i < 0 or i >= len(self._components):
            raise ValueError("Invalid index")
        if not self._components[i].contains(e):
            raise ValueError("Element not in the specified component")
        return (i, e)
   
       
   
    def unpack(self, e: E) -> Tuple[int, C]:
        return e
    
    
    def load(self, h: I.IOHelper, o: I.ConcreteRepr) -> List[C]:
        return cast(List[C], o)
    def save(self, h: I.IOHelper, x: List[C]) -> I.ConcreteRepr:
        return cast(I.ConcreteRepr, x)


class SolFiniteMakeSetDisjointUnion(I.FiniteMakeSetDisjointUnion):
    def disjoint_union(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetDisjointUnion[X, Any]:
        
        return MyFiniteSetDisjointUnion(components) # implement here

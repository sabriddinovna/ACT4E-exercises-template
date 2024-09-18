from typing import Any, TypeVar, cast, Collection, Iterator, List

import act4e_interfaces as I
# imagine you have a set A, we need to construct powerset P
X = TypeVar("X")
E = TypeVar("E")#elements of P
C = TypeVar("C") #elements of A

class MyFiniteSetOfFiniteSubsets(I.FiniteSetOfFiniteSubsets):
    _elements: Collection[C]

    def __init__(self, elements:Collection[C] ):
        self._elements= list(elements)
    
    #set of subsets
    def contents(self, e: E) -> Iterator[C]:
        return iter(e)       #getting an element of powerset and returning an iterator of elements of A
    def construct(self, elements: Collection[C]) -> E:
        return elements    #getting bunch of elements of A, and constructing a subset of A
    
    
    #finite set
    def size(self) -> int:
        return len(self.elements)
    def elements(self) -> Iterator[E]:
        return iter(self.elements)
    

    #setoid
    def contains(self, x: Any) -> bool:
        for y in self._elements:
            if self.equal(x,y):
                return True
        return False
    def save(self, h: I.IOHelper, x: Any) -> I.ConcreteRepr:
        return cast(I.ConcreteRepr, x)
    def load(self, h: I.IOHelper, o: I.ConcreteRepr) -> E:
        return cast(E,o)



class SolFiniteMakePowerSet(I.FiniteMakePowerSet):
    def powerset(self, s: I.FiniteSet[X]) -> I.FiniteSetOfFiniteSubsets[X, Any]:
        elems=list(s.elements())

        def powset(elems):
            if len(elems)==0:
                yield []
            
            else:
                for item in (powset(elems[1:])):
                    yield [elems[0]]+item
                    yield item                                                     
        return MyFiniteSetOfFiniteSubsets([e for e in powset(elems)])


        

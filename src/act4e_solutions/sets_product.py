
from typing import Sequence, cast, Collection, Iterator, List, TypeVar, Any
import act4e_interfaces as I


from .my_finite_set import MyFiniteSet
from .sets_properties import SolFiniteSetProperties

C = TypeVar("C")

class MyFiniteSetProduct(I.FiniteSetProduct[C, List[C]]):
    _components: List[I.FiniteSet[C]]
    def __init__(self, components: Sequence[I.FiniteSet[C]]):
        self._components = list(components)

    def components(self) -> Sequence[I.FiniteSet[C]]:
        return self._components
    
    def contains(self, x: List[C]) -> bool:
        if not isinstance(x, List):
            return False
        for elem, comp in zip(x, self._components):
            if not comp.contains(elem):
                return False
        
        return True

    def size(self) -> int:
        ans = 1
        for c in self._components:
            ans *= c.size()
        return ans
    
    def elements(self) -> Iterator[List[C]]:
        result = [[]]

        for comp in self._components:
            temp_result = []

            for item in result:
                for elem in comp.elements():
                    temp_result.append(item + [elem])
            result = temp_result
        
        for product in result:
            yield product
    
    def pack(self, args: Sequence[C]) -> List[C]:
        return list(args)
    def unpack(self, args: List[C]) -> Sequence[C]:
        return args

    def load(self, h: I.IOHelper, o: I.ConcreteRepr) -> List[C]:
        return cast(List[C], o)
    def save(self, h: I.IOHelper, x: List[C]) -> I.ConcreteRepr:
        return cast(I.ConcreteRepr, x)





class MyFiniteSetRepresentation(I.FiniteSetRepresentation):
    def load(self, h: I.IOHelper, data: I.FiniteSet_desc) -> I.FiniteSet[Any]:
        if not isinstance(data, dict):
            raise I.InvalidFormat()
        if "elements" in data:
            if not isinstance(data["elements"], list):
                raise I.InvalidFormat()
            elements = data["elements"]
            return MyFiniteSet(elements)
        elif "product" in data:
            if not isinstance(data["product"], list):
                raise I.InvalidFormat()
            components = [self.load(h, comp) for comp in data["product"]]
            return MyFiniteSetProduct(components)
        else:
            raise I.InvalidFormat()

    def save(self, h: I.IOHelper, f: I.FiniteSet[Any]) -> I.FiniteSet_desc:
        if isinstance(f, I.FiniteSetProduct):
            result = [self.save(h, x) for x in f.components()]
            return {"product": result}
        
        elif isinstance(f, I.FiniteSet):
            all_elements = [f.save(h, elem) for elem in f.elements()]
            return {"elements": all_elements}
            


X = TypeVar("X")


class SolFiniteMakeSetProduct(I.FiniteMakeSetProduct):

    def product(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetProduct[X, Any]:
        return MyFiniteSetProduct(components)











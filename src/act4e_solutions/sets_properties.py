from typing import Any, overload, Sequence, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolFiniteSetProperties(I.FiniteSetProperties):
    def is_subset(self, a: I.FiniteSet[X], b: I.FiniteSet[X]) -> bool:
        return all([b.contains(x) for x in a.elements()])
    def equal(self, a : I.FiniteSet[X], b:I.FiniteSet[X])-> bool:
        return self.is_subset(a,b) and self.is_subset(b,a)
    
    def is_strict_subset(self, a: I.FiniteSet[X], b: I.FiniteSet[X]) -> bool:
        return self.is_subset(a,b) and not self.is_subset(b,a)

class SolFiniteMakeSetUnion(I.FiniteMakeSetUnion):
    def union(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetUnion[X, Any]:
        
        union=set()
        for element in components:
            for a in element:
                union.add(a)

        return I.FiniteSetUnion(union)



class SolFiniteMakeSetIntersection(I.FiniteMakeSetIntersection):
    def intersection(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSet[X]:
        
        if not components:
            raise ValueError("Components sequence is empty")
        
        # Initialize intersection with the elements of the first set
        intersection_set = set(components[0])
        
        # Perform intersection with each subsequent set
        for element in components[1:]:
            intersection_set.intersection_update(element)  # In-place intersection
        
        # Return the result as an instance of I.FiniteSet[X]
        return I.FiniteSet(intersection_set)
        

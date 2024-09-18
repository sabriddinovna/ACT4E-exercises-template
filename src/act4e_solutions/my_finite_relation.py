from typing import Generic, TypeVar, Dict, Set, Tuple
import act4e_interfaces as I

E1 = TypeVar("E1")
E2 = TypeVar("E2")

class MyFiniteRelation(I.FiniteRelation[E1, E2]):
    def __init__(self, source_set: I.FiniteSet[E1], target_set: I.FiniteSet[E2], relations: Set[Tuple[E1, E2]]):
        self._source_set = source_set
        self._target_set = target_set
        self._relations = relations

    def source(self) -> I.FiniteSet[E1]:
        return self._source_set

    def target(self) -> I.FiniteSet[E2]:
        return self._target_set

    def holds(self, e1: E1, e2: E2) -> bool:
        return (e1, e2) in self._relations

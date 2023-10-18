from typing import Any, TypeVar

import act4e_interfaces as I
A = TypeVar("A")
B = TypeVar("B")


class SolFiniteSemigroupMorphismsChecks(I.FiniteSemigroupMorphismsChecks):
    def is_semigroup_morphism(self, a: I.FiniteSemigroup[A], b: I.FiniteSemigroup[B], f: I.FiniteMap[A, B]) -> bool:
        raise NotImplementedError

    def is_monoid_morphism(self, a: I.FiniteMonoid[A], b: I.FiniteMonoid[B], f: I.FiniteMap[A, B]) -> bool:
        raise NotImplementedError

    def is_group_morphism(self, a: I.FiniteGroup[A], b: I.FiniteGroup[B], f: I.FiniteMap[A, B]) -> bool:
        raise NotImplementedError

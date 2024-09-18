from typing import Any, TypeVar

import act4e_interfaces as I
from act4e_interfaces import FiniteRelation

E1 = TypeVar("E1")
E2 = TypeVar("E2")
E3 = TypeVar("E3")
E = TypeVar("E")

A = TypeVar("A")
B = TypeVar("B")


class SolFiniteRelationProperties(I.FiniteRelationProperties):
    def is_surjective(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        codomain=fr.codomain().elements() #elements of B
        relation=fr.elements() #pairs which aRb
        mapped=set(b for (_,b) in relation)
        return all(b in mapped for b in codomain)

    def is_defined_everywhere(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        domain=fr.domain().elements()
        relation=fr.elements() #xRy
        mapped= set(x for (x,_) in relation)
        return all( x in mapped for x in domain)
        

    def is_injective(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_single_valued(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()


class SolFiniteRelationOperations(I.FiniteRelationOperations):
    def transpose(self, fr: I.FiniteRelation[A, B]) -> I.FiniteRelation[B, A]:
        raise NotImplementedError()

    def as_relation(self, f: I.FiniteMap[A, B]) -> I.FiniteRelation[A, B]:
        raise NotImplementedError()


class SolFiniteEndorelationProperties(I.FiniteEndorelationProperties):
    def is_reflexive(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_irreflexive(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_transitive(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_symmetric(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_antisymmetric(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_asymmetric(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()


class SolFiniteEndorelationOperations(I.FiniteEndorelationOperations):
    def transitive_closure(self, fr: I.FiniteRelation[E, E]) -> I.FiniteRelation[E, E]:
        raise NotImplementedError()


class SolFiniteRelationCompose(I.FiniteRelationCompose):
    def compose(self, fr1: FiniteRelation[E1, E2], fr2: FiniteRelation[E2, E3]) -> I.FiniteRelation[E1, E3]:
        raise NotImplementedError()

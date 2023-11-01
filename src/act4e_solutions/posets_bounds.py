from typing import Any, List, Optional, overload, TypeVar, Collection

import act4e_interfaces as I

E = TypeVar("E")
X = TypeVar("X")

class SolFinitePosetMeasurement(I.FinitePosetMeasurement):
    def height(self, fp: I.FinitePoset[Any]) -> int:
        raise NotImplementedError()

    def width(self, fp: I.FinitePoset[Any]) -> int:
        raise NotImplementedError()


class SolFinitePosetConstructionOpposite(I.FinitePosetConstructionOpposite):
    def opposite(self, p: I.FinitePoset[X]) -> I.FinitePoset[X]:
        raise NotImplementedError() # implement here


class SolFinitePosetSubsetProperties(I.FinitePosetSubsetProperties):
    def is_chain(self, fp: I.FinitePoset[X], s: Collection[X]) -> bool:
        raise NotImplementedError()

    def is_antichain(self, fp: I.FinitePoset[X], s: Collection[X]) -> bool:
        raise NotImplementedError()


class SolFinitePosetSubsetProperties2(I.FinitePosetSubsetProperties2):
    def is_lower_set(self, fp: I.FinitePoset[X], s: List[X]) -> bool:
        raise NotImplementedError()

    def is_upper_set(self, fp: I.FinitePoset[X], s: List[X]) -> bool:
        raise NotImplementedError()


class SolFinitePosetClosures(I.FinitePosetClosures):
    def upper_closure(self, fp: I.FinitePoset[X], s: List[X]) -> List[X]:
        raise NotImplementedError()

    def lower_closure(self, fp: I.FinitePoset[X], s: List[X]) -> List[X]:
        raise NotImplementedError()


class SolFinitePosetInfSup(I.FinitePosetInfSup):
    def lower_bounds(self, fp: I.FinitePoset[E], s: List[E]) -> List[E]:
        raise NotImplementedError()

    def upper_bounds(self, fp: I.FinitePoset[E], s: List[E]) -> List[E]:
        raise NotImplementedError()

    def infimum(self, fp: I.FinitePoset[E], s: List[E]) -> Optional[E]:
        raise NotImplementedError()

    def supremum(self, fp: I.FinitePoset[E], s: List[E]) -> Optional[E]:
        raise NotImplementedError()


class SolFinitePosetMinMax(I.FinitePosetMinMax):
    def minimal(self, fp: I.FinitePoset[E], S: List[E]) -> List[E]:
        raise NotImplementedError()

    def maximal(self, fp: I.FinitePoset[E], S: List[E]) -> List[E]:
        raise NotImplementedError()

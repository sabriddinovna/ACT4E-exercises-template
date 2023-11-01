from typing import Callable, Generic, Optional, TypeVar

import act4e_interfaces as I
from act4e_interfaces import EnumerableSet

OD = TypeVar("OD")
MD = TypeVar("MD")


class SolSemiCategoryRepresentation(I.SemiCategoryRepresentation):
    def load(
        self,
        h: I.IOHelper,
        data: I.FiniteSemiCategory_desc,
        ObData: I.Setoid[OD],
        MorData: I.Setoid[MD],
        compose: Callable[[OD, OD, OD, MD, MD], MD],
    ) -> I.SemiCategory[I.RichObject[OD], I.RichMorphism[MD]]:
        raise NotImplementedError()


class SolSemiCategory(Generic[OD, MD], I.SemiCategory[I.RichObject[OD], I.RichMorphism[MD]]):
    """ Skeleton for a class implementing SemiCategory."""

    def __init__(
        self,
        add, more, parameters, here
    ):
        raise NotImplementedError

    def objects(self, uptolevel: Optional[int] = None) -> EnumerableSet[OD]:
        raise NotImplementedError

    def hom(self, ob1: OD, ob2: OD, uptolevel: Optional[int] = None) -> EnumerableSet[MD]:
        raise NotImplementedError

    def compose(self, ob1: OD, ob2: OD, ob3: OD, m1: MD, m2: MD) -> MD:
        raise NotImplementedError

    def identity(self, ob: OD) -> MD:
        raise NotImplementedError

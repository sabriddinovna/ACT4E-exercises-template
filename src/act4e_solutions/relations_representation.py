# from typing import TypeVar

# import act4e_interfaces as I

# A = TypeVar("A")
# B = TypeVar("B")


# class SolFiniteRelationRepresentation(I.FiniteRelationRepresentation):
#     def load(self, h: I.IOHelper, data: I.FiniteRelation_desc) -> I.FiniteRelation[A, B]:
#         raise NotImplementedError()

#     def save(self, h: I.IOHelper, f: I.FiniteRelation[A, B]) -> I.FiniteRelation_desc:
#         raise NotImplementedError()


from typing import Dict, Tuple, Any, cast, List
import act4e_interfaces as I
from .my_finite_relation import MyFiniteRelation
from .my_finite_set import MyFiniteSet


class FiniteRelationRepresentation(I.FiniteRelationRepresentation):
    def load(self, h: I.IOHelper, data: I.FiniteRelation_desc) -> I.FiniteRelation[Any, Any]:
        # Ensure the data is a dictionary
        # if not isinstance(data, I.FiniteRelation_desc):
        #     raise I.InvalidFormat()

        # Extract source elements, target elements, and relations
        source_elements = data.get('source', [])
        target_elements = data.get('target', [])
        relations = data.get('relations', [])

        # Ensure correct types
        # if not isinstance(source_elements, I.FiniteSet_desc) or not isinstance(target_elements, I.FiniteSet_desc) or not isinstance(relations, I.List[I.List[I.ConcreteRepr]]):
        #     raise I.InvalidFormat() 

        # Convert lists to sets for source and target
        # source_set = MyFiniteSet(source_elements)
        # target_set = MyFiniteSet(target_elements)

        # Convert relation list of lists to a set of tuples
        # relation_tuples = set(tuple(relation) for relation in relations)

        # Create and return the FiniteRelation
        return MyFiniteRelation(source_elements, target_elements, relations)

    def save(self, h: I.IOHelper, f: I.FiniteRelation[Any, Any]) -> I.FiniteRelation_desc:
        # source_elements = cast(I.FiniteSet_desc, f.source())
        # target_elements = cast(I.FiniteSet_desc, f.target())
        # relations = cast(List[List[I.ConcreteRepr]], f._relations)

        return cast(I.FiniteRelation_desc, {
            'source': f.source(),
            'target': f.target(),
            'relations': f._relations
        })

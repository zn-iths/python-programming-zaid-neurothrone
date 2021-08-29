from abc import ABC


class Field(ABC):
    """The Field object has a resource type and value.

    Args:
        type_ (str): the type of resource.
        resource (int): the amount of resource.

    Attributes:
        type_ (str): the resource type of this Field.
        resource (int): the amount of resources in the Field.
        name (str): the name of the Field class or subclass.
    """

    PRODUCTION_RATE = 4
    """The rate of increase in resource value (int)."""

    def __init__(self, type_: str, resource: int = 0) -> None:
        self.type = type_
        self.resource = resource
        self.name = "Field"

    @property
    def resource(self) -> int:
        return self._resource

    @resource.setter
    def resource(self, resource: int) -> None:
        if resource >= 0:
            self._resource = resource

    def __add__(self, other: "Field") -> None:
        self.resource += other.resource

    def __sub__(self, other: "Field") -> None:
        self.resource -= other.resource

    def __str__(self) -> str:
        return f"{self.name} field has a resource type of {self.resource} " \
               f"with a value of {self.resource}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.type}, {self.resource})"

    def produce(self) -> None:
        """Adds the current value of the resource with the production rate"""

        self.resource += Field.PRODUCTION_RATE


class Clay(Field):
    """The Clay Field object has a resource type and value.

    Args:
        resource (int): the amount of resource.

    Attributes:
        name (str): the name of the Field subclass.
    """

    def __init__(self, resource: int = 0):
        super().__init__(type_=ResourceType.CLAY, resource=resource)
        self.name = ResourceType.CLAY.capitalize()


class Crop(Field):
    """The Crop Field object has a resource type and value.

        Args:
            resource (int): the amount of resource.

        Attributes:
            name (str): the name of the Field subclass.
        """

    def __init__(self, resource: int = 0):
        super().__init__(type_=ResourceType.CROP, resource=resource)
        self.name = ResourceType.CROP.capitalize()


class Iron(Field):
    """The Iron Field object has a resource type and value.

        Args:
            resource (int): the amount of resource.

        Attributes:
            name (str): the name of the Field subclass.
        """

    def __init__(self, resource: int = 0):
        super().__init__(type_=ResourceType.IRON, resource=resource)
        self.name = ResourceType.IRON.capitalize()


class Lumber(Field):
    """The Lumber Field object has a resource type and value.

        Args:
            resource (int): the amount of resource.

        Attributes:
            name (str): the name of the Field subclass.
        """

    def __init__(self, resource: int = 0):
        super().__init__(type_=ResourceType.LUMBER, resource=resource)
        self.name = ResourceType.LUMBER.capitalize()


class ResourceType:
    """The possible types a resource of a Field can have."""

    CLAY = "clay"
    CROP = "crop"
    IRON = "iron"
    LUMBER = "lumber"

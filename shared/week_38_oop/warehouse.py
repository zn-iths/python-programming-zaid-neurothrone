from shared.week_38_oop.field import Field
from shared.week_38_oop.field import ResourceType


class Warehouse:
    """The Warehouse object has fields and resource values.

    Args:
        fields (Field): the variable arguments for Field objects.

    Attributes:
        fields (list[Field]): List of field objects.
        stock (dict[str, int]): Dictionary of resource type names and their values.
    """

    MAX_CAPACITY = 800
    """The maximum storage value of each resource type."""

    def __init__(self, *fields: "Field") -> None:
        self.fields: list["Field"] = [*fields]
        self.stock: dict[str, int] = {
            ResourceType.CLAY: 0,
            ResourceType.CROP: 0,
            ResourceType.IRON: 0,
            ResourceType.LUMBER: 0,
        }
        self.update_stock()

    def __repr__(self) -> str:
        return f"Warehouse({self.fields})"

    def __str__(self) -> str:
        return f"Warehouse current stock:\n" \
               f"Clay:   {self.stock[ResourceType.CLAY]}\n" \
               f"Crop:   {self.stock[ResourceType.CROP]}\n" \
               f"Iron:   {self.stock[ResourceType.IRON]}\n" \
               f"Lumber: {self.stock[ResourceType.LUMBER]}"

    def print_current_stock(self) -> None:
        """Prints the return value of the instance's __str__() method."""

        print(self)

    def update_stock(self) -> None:
        """Updates the storage of each resource type."""

        for field in self.fields:
            self.stock[field.type] += field.resource
            field.resource = 0
            if self.stock[field.type] > Warehouse.MAX_CAPACITY:
                self.stock[field.type] = Warehouse.MAX_CAPACITY

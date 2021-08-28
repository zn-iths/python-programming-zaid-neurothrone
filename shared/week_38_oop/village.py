from shared.week_38_oop.field import Clay
from shared.week_38_oop.field import Crop
from shared.week_38_oop.field import Field
from shared.week_38_oop.field import Iron
from shared.week_38_oop.field import Lumber
from shared.week_38_oop.warehouse import Warehouse


class Village:
    """The village object has a warehouse which has fields.

    Args:
        *fields (Field): the variable arguments for Field objects..

    Attributes:
        warehouse (Warehouse): the object that has the Fields.
    """

    def __init__(self, *fields: "Field") -> None:
        if len(fields) > 0:
            self.warehouse = Warehouse(*fields)
        else:
            self.warehouse = Warehouse(Clay(), Crop(), Iron(), Lumber())

    def __repr__(self) -> str:
        return f"Village()"

    def __str__(self) -> str:
        return f"Village has a Warehouse with a max capacity of {Warehouse.MAX_CAPACITY}" \
               f" and fields with a production rate of {Field.PRODUCTION_RATE} per hour.\n" \
               f"{self.warehouse}"

    def skip_hour(self):
        """Calls the produce() method of each field in the warehouse.

        Increases the current resource value of each field by the
        production rate and updates the warehouse's stock.
        """

        for field in self.warehouse.fields:
            field.produce()
        self.warehouse.update_stock()

    def print_village_status(self) -> None:
        """Prints the return value of the instance's __str__() method."""
        print(self)

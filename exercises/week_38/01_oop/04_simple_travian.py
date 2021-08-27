from abc import ABC
from platform import system

from colorama import Fore
from colorama import init

if (system()) == "Windows":
    init()  # make colorama works for windows


class ResourceType:
    """The possible types a resource of a Field can have."""

    CLAY = "clay"
    CROP = "crop"
    IRON = "iron"
    LUMBER = "lumber"


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
        return f"{self.name}({self.resource})"

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


def print_menu() -> None:
    """Prints the menu of this program."""

    print(f"{Fore.CYAN}---------------------------------")
    print("1. List current stock of Warehouse")
    print("2. List general status of Village")
    print("3. Skip 1 hour")
    print("0. Quit")
    print(f"---------------------------------{Fore.RESET}")


def get_int_input(min_: int, max_: int) -> int:
    """Get integer based user input.

    Args:
        min_ (int): The minimum acceptable int value.
        max_ (int): The maximum acceptable int value.

    Returns:
        int: the integer input from the user
    """
    while True:
        try:
            user_input = int(input("Enter your selection: "))
            if min_ <= user_input <= max_:
                return user_input
            else:
                print(f"{Fore.RED}[Error]: {Fore.RESET}Invalid selection. Try again.")
        except ValueError:
            print(f"{Fore.RED}[Error]: {Fore.RESET}Invalid input. Only enter an integer.")


def run() -> None:
    """Initializes the program and runs it's loop."""

    village = Village()
    menu_actions: dict = {
        1: village.warehouse.print_current_stock,
        2: village.print_village_status,
        3: village.skip_hour
    }

    print("---- Welcome to Travian Mini ----")

    is_running = True
    while is_running:
        print_menu()
        if (selection := get_int_input(min_=0, max_=len(menu_actions) - 1)) == 0:
            break
        menu_actions[selection]()
    print(f"{Fore.CYAN}Terminating program...")


if __name__ == "__main__":
    run()

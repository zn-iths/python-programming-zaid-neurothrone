class Unit:
    """"""
    INCH_TO_CM = 2.54
    CM_TO_INCHES = 0.393701
    FOOT_TO_METERS = 0.3048
    METERS_TO_FEET = 3.28084
    POUND_TO_KG = 0.453592
    KG_TO_POUND = 2.20462

    def __init__(self, value: float) -> None:
        self.value = value

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float) -> None:
        if value is None:
            raise ValueError("Unit has no value.")
        elif value < 0:
            raise ValueError("Value can not be less than 0.")
        self._value = value

    @value.deleter
    def value(self) -> None:
        self.value = None

    def inches_to_cm(self) -> float:
        return self.value * Unit.INCH_TO_CM

    def cm_to_inches(self) -> float:
        return self.value * Unit.CM_TO_INCHES

    def foot_to_meters(self) -> float:
        return self.value * Unit.FOOT_TO_METERS

    def meters_to_feet(self) -> float:
        return self.value * Unit.METERS_TO_FEET

    def pound_to_kg(self) -> float:
        return self.value * Unit.POUND_TO_KG

    def kg_to_pound(self) -> float:
        return self.value * Unit.KG_TO_POUND

    def __repr__(self) -> str:
        return f"Unit({self.value})"


class Person:
    def __init__(self, name: str, age: int, email: str) -> None:
        self.name = name
        self.age = age
        self.email = email

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError("Name argument must be a string.")
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        if 0 < age < 125:
            self._age = age
        else:
            raise ValueError("Age must be an integer between 0 and 125.")

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        if "@" not in email:
            raise ValueError("Email must include '@'.")
        self._email = email

    def __repr__(self) -> str:
        return f"Person({self.name}, {self.age}, {self.email})"

    def __str__(self) -> str:
        return f"Person named {self.name}, {self.age} years old and has an email of {self.email}"

    def say_hello(self) -> None:
        print(f"Hi, my name is {self.name}, I am {self.age} years old, my email "
              f"address is {self.email}.")

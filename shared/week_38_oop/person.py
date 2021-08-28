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

"""
Day 1 - Python core concepts quick tour.
Run: python concepts.py
"""

"""
This is called type hinting the name of the variable comes before 
':' and then sets the 'Expected type' to its 'Expected Value'
"""
an_int: int = 42
a_float: float = 3.4
a_str: str = "hello"
a_bool: bool = True

"""
Takes the value of 'n' operates on 'n' using the 
the conditionals below once. Then takes the 
value of 'n' and matches 
the string value like "FizzBuzz" and returns that string value. 
"""


def fizzbuz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


"""
This function takes a list of integer values addes them to zero
returns that value
"""


def sum_list(xs: list[int]) -> int:
    total = 0
    for x in xs:
        total += x
    return total


"""
String interpolation example of hello, world
"""


def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


"""
Python special way to intialize a new object with '_init_' its
a reserved name in python, its like the constructor in C# allowing 
you to declare your fields like 'private readonly string _somestring;' and
then constructing it in within the same method for variable acess through
'self' across the whole class just using a method example 


C# example: 

public class Vehicle
{
    private string _name;
    private int _speed;
    
    public Vehicle(string name)
    {
        _name = name;
        _speed = 0;
    }
}

// Usage
Vehicle myCar = new Vehicle("Toyota");


python same ex:

class Something:
    def _init_(self, name: str, age: int):
    self.name = name
    self.age = age

def get_some_name(self):
    return f"Hello, {self.name}, your age is {self.age}"

some_object = Something("Zack",22)
print(some_object.get_some_name())



"""


class Vehicle:
    # instance variables
    def __init__(self, name: str):
        self._name = name  # intialized to name parameter
        self._speed = 0  # intialized to zero

    def accelerate(self, delta: int) -> None:
        self._speed += delta

    def info(self) -> str:
        return f"{self._name} going {self._speed} km/h"


class Car(Vehicle):
    def honk(self) -> str:
        return "beep!"


def describe_vehicle(v: Vehicle) -> str:
    return v.info()


if __name__ == "__main__":
    print(greet())
    print([fizzbuz(i) for i in range(1, 16)])
    print("sum_list:", sum_list([1, 2, 3, 4, 5]))
    car = Car("Zippy")
    car.accelerate(20)
    print(describe_vehicle(car))

def demo_struct():
    """
    Example of an 'List data structure' -
    should return [1,2,5,9]
    """
    nums = [5, 2, 9]
    nums.append(1)
    nums.sort()

    """
    The coordinate system in Python tuples is actually more like a standard mathematical grid:

The first number (10) represents the horizontal position (x-axis)
The second number (20) represents the vertical position (y-axis)

# This works:
point = (10, 20)
print(point[0])  # prints: 10
print(point[1])  # prints: 20

# This doesn't work:
# point[0] = 30  # Error! Tuples are immutable
This immutability is useful when you need to ensure 
that coordinates don't accidentally get changed, 
like when you're tracking positions in a game or 
storing map locations.
    """
    point = (10, 20)

    """
    Example of a 'Hash set data structure' - 
    Tags is assigned to a set object, the .add() function adds a single element to the 
    the string value to the set object but if the string value already exist for the set object 
    .add method will do nothing as sets only store 'UNIQUE' numbers ->'{}'
    """
    tags = {"ml", "quantum", "python"}
    tags.add("ml")
    has_quantum = "quantum" in tags  # checking if quantum is on the list

    """
    This is a dictionary data structure '"Key": value'
    """
    metrics = {"accuracy": 0.9, "loss": 0.3}
    metrics["loss"] = 0.25

    return {
        "nums": nums,
        "point": point,
        "tags": sorted(tags),
        "has_quantum": has_quantum,
        "metrics": metrics,
    }

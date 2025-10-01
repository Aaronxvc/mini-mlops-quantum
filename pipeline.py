"""
Minimal pipeline skeleton for Iris.

The Pipeline's Job
The pipeline is like a flower sorting system:

First, it collects all your flowers (load_dataset):
Either from your CSV file or from the built-in iris dataset
Organizes them into a neat collection
Then it splits them into groups (split_data):
Puts 80% in the training pile
Puts 20% in the testing pile
Makes sure each pile has the same mix of flower types
Why This Matters
This splitting is crucial because:

The training group teaches the system what to look for
The testing group proves if the system learned correctly
It's like having a separate quiz to grade your student's knowledge
"""

"""
the pathlib.Path class provides an object-oriented way 
to interact with the file system.

Convenience Methods: It offers numerous methods for common tasks, such as:
exists(): Check if a path exists.
is_file(), is_dir(): Check if it's a file or directory.
parent, name, stem, suffix: Access different parts of the path.
joinpath(): Concatenate path components.
mkdir(), touch(), unlink(): Create or delete files and directories.
read_text(), write_text(): Read from and write to text files.
"""
from pathlib import Path

"""
tuple is a built-in data type used to store collections of data. It is an ordered, immutable sequence of elements.
Tuples are typically created by placing items inside parentheses () and separating them with commas.
Python

'This is a tuple -> ()' items/emelemts within are immutable(Non changing)

# An empty tuple
empty_tuple = ()

# A tuple with mixed data types
my_tuple = ("apple", 1, True, 3.14)

# A tuple with a single item (note the comma)
single_item_tuple = ("orange",) 
"""
from typing import Tuple

"""
In Python, pd is not a data type itself, but rather a 
widely adopted alias (a shorthand name) for the Pandas 
library.When you write import pandas as pd, 
you are importing the entire Pandas library and 
making it accessible through the shorter name pd. 
This allows you to call functions and access objects 
within the Pandas library using pd. instead of pandas., 
which is particularly convenient given the frequent use of 
Pandas in data analysis tasks.

"""
import pandas

"""
# In essence, load_iris provides a convenient way to 
# access a well-known, clean, and balanced dataset 
# that is excellent for learning and practicing 
# various machine learning algorithms, particularly 
# for classification and clustering tasks.
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

"""
csv_path is like asking 
"where's the book?" (it can be a path or None)
-> Tuple[pd.DataFrame, pd.Series] is like saying 
"I'll give you back two things: a table of data and a
 list of answers"
"""


# str | None means "this can be either a string or None"
def load_dataset(csv_path: str | None = None) -> Tuple[pandas.DataFrame, pandas.Series]:
    """
        First, they check if you brought your own book (CSV file)
    If not, they get a standard book (iris dataset)
    They organize the book's information into two piles (features and answers)
    They tell you how big each pile is
    They hand you both piles to work with
    """
    if csv_path and Path(csv_path).exists():
        df = pandas.read_csv(csv_path)
        X = df.drop(colums=df.colums[-1])
        y = df[df.colums[-1]]
    else:
        iris = load_iris(as_frame=True)
        X, y = iris.data, iris.target
    print(f"Loaded dataset: X={X.shape}, y={y.shape}")
    return X, y


def split_data(X, y, test_size: float = 0.2, random_state: int = 42):
    return train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )


def main(csv_path: str | None = None):
    print("[PIPELINE] starting...")
    X, y = load_dataset(csv_path)
    X_train, X_test, y_train, y_test = split_data(X, y)
    print(f"[PIPELINE] Split: X_train={X_train.shape}, X_test={X_test.shape}")
    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    main()

"""
So this is a 'binary search' example, binary searches are typically used for
Long list or arrays, this efficient algorthim allows you too
open to the mid of the complex List or array compare your element
with the stored middle element if there is not a match, then looks
at the left half for a match if its later look at the right half
for a match, keep doing this until you find it or run out of pages

"""

from typing import Sequence, Optional


def binary_search(sorted_seq: Sequence[int], target: int) -> Optional[int]:
    """This sets up our search boundaries:

    lo (low) is like the first page number
    hi (high) is like the last page number"""
    lo, hi = 0, len(sorted_seq) - 1
    """
    This is like opening to the middle page:

We keep searching as long as we have pages to look at
mid is the middle page number
    """
    while lo <= hi:
        mid = (lo + hi) // 2
        """
        This checks if we found what we're looking for:

If the middle word matches our target, we return its position
        """
        if sorted_seq[mid] == target:
            return mid
        """
        This narrows down our search:

If our target word comes later in the alphabet, we look in the right half
If it comes earlier, we look in the left half
        """
        if sorted_seq[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

        """
        This is returned if nothing is found at all
        """
    return None


if __name__ == "__main__":
    data = [1, 3, 4, 7, 9, 12, 20]
    for t in [4, 6, 20, -1]:
        print(t, "->", binary_search(data, t))

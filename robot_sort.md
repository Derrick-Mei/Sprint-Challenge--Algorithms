Basically I'm going to make implement bubble sort but going in both directions

loop from range(0, len(list))
  if even, go right swapping if item at that position is bigger
    stop when you've reached the end
  if odd, go left swapping if item at that position is smaller
    stop when you've reached None


I made some optimizations that might be running afoul of the rules
  1. I am using i to signify left or right, although I can use the light bulb for that.
  2. I am using len(self._list) to stop when I have already sorted the items to the right
  3. I passed i to is_sorted function.
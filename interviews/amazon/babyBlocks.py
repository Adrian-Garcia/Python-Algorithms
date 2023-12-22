"""
You have a collection of 'baby blocks' (cubes with single upper-case letters of the alphabet on each side). 
Each block could have up to six different letters on it, assume that each block only has two distinct letters.

Write a function that takes a collection of blocks and a target word and returns true or false 
depending on whether or not you can spell the target word with the collection of blocks.

Ex: (B,A),(A,B),(X,Y),(A,B): "BABY" => yes (B,A),(A,B),(L,E),(A,B): "ABLE" => no (since L and E are on the same block)


BABY
{
  (B,A),(B,A),(A,B),(X,Y),(A,B)
  (),(B,A),(A,B),(X,Y),(A,B)
    []
    
}

BABYS
{
  (B,A)(T,A)(B,S)(Y,Y)
  (),(B,A),(A,B),(X,Y),(A,B)
    []
    
}


{
    B -> [1,2,3,5]
    A -> [1,2,3,5]
    x -> [4]
    y -> [4]
}


{
    B -> [1,2,3]
    A -> [2]
    B -> [1,2,3]
    Y -> [4]
}


BABY
(B,A),(A,B),(A,B)

lettersInBLock = {
    B -> 2
    A -> 1
    Y -> 1
}

letterAbailableInBloack = {
    Y -> 1
    B -> 3
    A -> 3
}

"""

"""
BABYS

{
    (B,A) -> [1]
    (T,A) -> [2]
    (B,A) -> [3]
    (Y,Y) -> [4]
}

{
  (B,S)
}
"""


def babyBlocks(cubes, target):
    if len(cubes) < len(target):
        return False

    for letter in target:
        for i in range(len(cubes)):  # Bottleneck
            cube = cubes[i]
            if letter in cube:
                cubes.remove(i)
            else:
                return False

    return True

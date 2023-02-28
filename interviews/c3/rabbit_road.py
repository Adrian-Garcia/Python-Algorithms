"""
A road is divided into some number of units, and at each unit, there may or may
not exist a dangerous trap. Given a list of safe positions in sorted ascending
order, determine if the rabbit can pass the road by landing on the last safe
position.

Initially, a rabbit is in the first safe position and assumes its first jump
must be 1 unit.

If the previous jump was k units, its next jump must be either k - 1, k, or
k + 2 units. 

Assume the rabbit can only jump in the forward direction.

Example 1:
  _  _        _     _           _
  0  1  2  3  4  5  6  7  8  9  10  11 12 
  Path: 0 -> 1 -> 4 -> 6 -> 10
  Input: safe positions = [0, 1, 2, 4, 6, 10]
  Output: true

Example 2:
  _  _  _  _                 _      _
  0  1  2  3  4  5  6  7  8  9  10  11
  Input: safe positions = [0, 1, 2, 3, 9, 11]
  Output: false
"""


def road(safe_positions):
    stack = [1]
    jumps = [1]

    finish = safe_positions[len(safe_positions) - 1]
    visited = [False] * 100

    while stack:
        curr_position = stack.pop()
        prev_jump_size = jumps.pop()
        visited[curr_position] = True

        if curr_position == finish:
            return True

        next_jump_candidates = [prev_jump_size - 1, prev_jump_size, prev_jump_size + 2]

        while next_jump_candidates:
            next_jump_size = next_jump_candidates.pop()
            if (
                curr_position + next_jump_size in safe_positions
                and not visited[curr_position + next_jump_size]
            ):
                stack.append(curr_position + next_jump_size)
                jumps.append(next_jump_size)

    return False


safe_positions_1 = [0, 1, 2, 4, 6, 10]
safe_positions_2 = [0, 1, 2, 3, 9, 11]
print(road(safe_positions_1))

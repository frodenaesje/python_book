# file : ch_14_09_tower_of_hanoi_wiki_w_comments.py
# Tower of Hanoi solution based on Wikipedia description

def hanoi(n, source, dest, help):
    # Base case: When only one disk remains,
    # it can be moved directly from source to dest.
    # This is the stopping condition for ONE
    # branch of the recursion.
    # Note: The base case executes many times in total,
    # once for each branch in the recursion tree that
    # reaches n == 1.
    if n == 1:
        print(f"Move disk from {source} to {dest}")
        return

    # Step 1 in the recursive structure.
    # Before we can move the largest disk (disk n), we must
    # "clear the top":
    # Move the n−1 smaller disks from source to help.
    # Note that the roles of the pegs are SWAPPED: help becomes "dest"
    # in this subproblem, and dest becomes "help".
    # This rotation is essential to the algorithm.
    hanoi(n - 1, source, help, dest)

    # Step 2 in the recursive structure.
    # All smaller disks have been moved out of the way, and the
    # largest disk is now free.
    # We can therefore make "the big move":
    # move disk n to dest.
    # print() must appear exactly here because this move
    # must happen:
    # - after the top has been cleared (step 1)
    # - before we rebuild the tower (step 3)
    print(f"Move disk from {source} to {dest}")

    # Step 3 in the recursion.
    # After the largest disk has been moved, the
    # n−1 smaller disks must be moved from help to dest so
    # that they end up on top of the largest disk.
    # Again the pegs swap roles: help is now "source",
    # dest is "dest", and source acts as the temporary peg.
    # This step mirrors the first recursive call (step 1),
    # but now we are "rebuilding the tower" on dest.
    hanoi(n - 1, help, dest, source)

# Example call:
# Move 3 disks from A to C using B as auxiliary.
hanoi(3, "A", "C", "B")

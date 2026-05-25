def hanoi_solver(n):
    # Initialize the three rods
    # We use a list where the last element is the "top" of the rod.
    # The first rod starts with disks n down to 1.
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    # Helper function to capture state
    def get_state():
        return f"{rods[0]} {rods[1]} {rods[2]}"

    # Add the starting arrangement
    moves.append(get_state())

    def move_disk(n, source, target, auxiliary):
        if n > 0:
            # 1. Move n-1 disks from source to auxiliary
            move_disk(n - 1, source, auxiliary, target)
            
            # 2. Move the largest disk from source to target
            disk = rods[source].pop()
            rods[target].append(disk)
            moves.append(get_state())
            
            # 3. Move n-1 disks from auxiliary to target
            move_disk(n - 1, auxiliary, target, source)

    # Solve the puzzle: n disks, rods 0 to 2
    move_disk(n, 0, 2, 1)
    
    return "\n".join(moves)

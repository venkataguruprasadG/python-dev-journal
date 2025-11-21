def tower_of_hanoi(n, source, auxiliary, destination):

    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks from source to auxiliary peg, using destination as auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move the nth disk from source to destination peg
    print(f"Move disk {n} from {source} to {destination}")

    # Move n-1 disks from auxiliary to destination peg, using source as auxiliary
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Example usage:
num_disks = int(input("Enter the number of disks: "))
tower_of_hanoi(num_disks, "A", "B", "C")

"""
Towers of Hanoi
"""


def towers_of_hanoi(number_of_disks, start_peg=1, end_peg=3):
    if number_of_disks:
        towers_of_hanoi(
            number_of_disks - 1, start_peg, 6 - start_peg - end_peg
        )
        print(
            f"Move disk {number_of_disks} from peg {start_peg} to peg {end_peg}"
        )
        towers_of_hanoi(number_of_disks - 1, 6 - start_peg - end_peg, end_peg)


def tower_of_hanoi_v1(s, d, h, n):
    if n == 1:
        print(f"Moving plate {n} from {s} to {d}")
        return

    tower_of_hanoi_v1(s, h, d, n - 1)
    print(f"Moving plate {n} from {s} to {d}")
    tower_of_hanoi_v1(h, d, s, n - 1)


if __name__ == "__main__":
    towers_of_hanoi(number_of_disks=4)

    tower_of_hanoi_v1(s=1, h=2, d=3, n=4)

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


if __name__ == "__main__":
    towers_of_hanoi(number_of_disks=4)

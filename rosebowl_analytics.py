"""
Dayna Mitty Larm
Southern Utah University
CSIS-1300-01-SP23: Programming with Python

Coding Nine 
GitHub: https://github.com/ddmlarm/coding-nine
Requirements: Rowsebowl.txt located in folder with rosebowl_analytics.py 
"""

import os


def main():
    """
    Main Driver for the rosebowl_analytics.py program. 

    Reads a .txt file and adds one entry per winner to a dictionary. Then, 
    prints a summary of rosebowl winners who have won more than four games to 
    a scoreboard. 
    """

    rosebowl_file_lines = scan_rosebowl_filelines()  # Get a list[str]

    if rosebowl_file_lines is not None:

        # Sort the winners in order of most to least wins
        rosebowl_winners_desc = sort_rosebowl_winners(rosebowl_file_lines)

        # Print the results
        print_rosebowl_winners(rosebowl_winners_desc)


def scan_rosebowl_filelines():
    """
    Returns a list of type string scanned from a formatted .txt file.
    """

    try:
        rosebowl_file_path = "Rosebowl.txt"  # txt file path
        rosebowl_file = open(rosebowl_file_path, mode="r", encoding="utf-8")

        # Read the file to a list[str], excluding blank lines (\n)
        rosebowl_file_lines = rosebowl_file.read().splitlines()
        return rosebowl_file_lines

    except FileNotFoundError:
        print("\nERROR:", FileNotFoundError)
        print(f"       The File \"{rosebowl_file_path}\" does not exist in:")
        print(f"       {os.path.dirname(os.path.realpath(__file__))}\n")

        return None


def sort_rosebowl_winners(rosebowl_file_lines):
    """
    Returns a sorted list of tuples representing winners of the rosebowl in 
    descendng order, from mnumber of most won to least one games.

    Keyword arguments:
        rosebowl_file_lines -- a list[str] representing winners of the rosebowl 
        and number of times won.
    """

    rosebowl_winners = dict()

    for winner in rosebowl_file_lines:
        if winner in rosebowl_winners:
            win_count = rosebowl_winners.get(winner)
            rosebowl_winners.update({winner: win_count+1})
        else:
            rosebowl_winners.update({winner: 1})

    rosebowl_winners_desc = sorted(rosebowl_winners.items(),
                                   key=lambda item: item[1],
                                   reverse=True)

    return rosebowl_winners_desc


def print_rosebowl_winners(rosebowl_winners_desc):
    """
    Prints the winners of the rosebowl who have won more than four games to the 
    console. 

    Keyword arguments:
        rosebowl_winners_desc -- a sorted list of tuples representing rosebowl 
        winners and their number of times won.
    """

    team_index = 0
    win_count_index = 1

    minimum_wins = 4
    print("\nROSE BOWL WINNERS ~2014")
    print("                   (4+)\n")
    print("Team               Wins")
    print("-----------------------")

    for winner in rosebowl_winners_desc:
        if winner[win_count_index] > minimum_wins:
            print(f"{winner[team_index]:<20}{winner[win_count_index]}")

    print("-----------------------\n")


# Main Driver
main()

# NOTES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# The exception handling for this program was relatively simple, with only one
# FileNotFoundError being caught. In addition to this I added my own protection
# to make sure the results returned from the function scanning the file would
# not be passed to another function if they were null.

# For this assignment I chose to use some more specific functions of python to
# do my conversions, such as using a lambda to sort the winners in descending
# order and f strings to format my results nicely. While I normaly define
# constants for formatting information parsed in from external files, the text
# file and results were nto complex enough to warrant the additional code.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

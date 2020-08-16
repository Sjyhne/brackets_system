from math import log2, floor
from bracket.bracket import Bracket
from node.node import Node

"""
    Function that based on the count of the teams, returns the number of list spaces that is needed in order to generate a bracket that has enough room for them all.
"""
def count_of_leaves_to_tree_size(count):
    log = log2(count)

    if (log % 1 == 0):
        return int(2**(log + 1) - 1)

    log = floor(log)

    diff = count - 2**log

    extra_nodes = diff * 2

    return int(2**(log + 1) - 1 + extra_nodes)

    
teams = ["Sander", "Morten", "Jørgen", "Erlend", "Per", "Hans", "Jan", "Knut"]

bracket = Bracket(tournament_name="CS:GO SAUDA TOURNAMENT")

size_of_places = count_of_leaves_to_tree_size(len(teams))

nodes = [Node(match_nr=x) for x in range(size_of_places)]

bracket.initiate_matches(nodes, teams)

bracket.print_matches()
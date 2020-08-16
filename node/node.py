from bracket.bracket import Bracket


class Node:
    def __init__(self, match_nr, t1 = None, t2 = None, winner = None, next_node = None, bracket = Bracket(tournament_name="No tournament")):
        self.match_nr = match_nr
        self.t1 = t1
        self.t2 = t2
        self.winner = winner
        self.next_node = next_node
        self.bracket = bracket

    def set_winner(self, winner):
        self.winner = winner

        if self.match_nr % 2 == 0:
            self.next_node.set_t2(self.winner)
        else:
            self.next_node.set_t1(self.winner)
    
    def set_next_node(self, node):
        self.next_node = node

    def set_t1(self, t1):
        self.t1 = t1
    
    def set_t2(self, t2):
        self.t2 = t2
    
    def __str__(self):
        return f"Match nr {self.match_nr}, Team 1: {self.t1}, Team 2: {self.t2}, Winner: {self.winner}, Next node: {self.next_node.match_nr}, Bracket: {self.bracket.tournament_name}"
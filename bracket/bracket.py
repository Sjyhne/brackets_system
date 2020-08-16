

class Bracket:
    def __init__(self, tournament_name):
        self.tournament_name = tournament_name
    
    def set_team_count(self, team_count):
        self.team_count = team_count

    def initiate_matches(self, matches, teams):
        self.matches = matches

        count = 0

        for match in reversed(self.matches):
            if (self.matches.index(match) == 0):
                match.set_next_node(match)
                break
            if count < len(teams):
                match.set_t1(teams[count])
            match.set_next_node(self.matches[(matches.index(match) - 1)//2])
            count += 1
        
        for match in self.matches:
            if match.t1 is not None and match.t2 is None:
                if match.match_nr % 2 == 0:
                    match.next_node.set_t2(match.t1)
                else:
                    match.next_node.set_t1(match.t1)
    
    def print_matches(self):
        for match in self.matches:
            if match.t1 is not None and match.t2 is not None and match.winner is None:
                print(match)
    
    def __str__(self):
        return f"{self.tournament_name} ({self.team_count})"

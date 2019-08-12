class Baseball_Team:
    def __init__(self,name,win,lose,draw):
        self.name=name
        self.win=win
        self.lose=lose
        self.draw=draw
        
    def calc_win_rate(self,win,lose):
        rate=win/(win+lose)
        return rate
    
    def show_team_result(self):
        rate=self.calc_win_rate(self.win,self.lose)
        print("{0:8s}".format(self.name),"{0:3d}".format(self.win),"{0:3d}".format(self.lose),"{0:3d}".format(self.draw),"{0:.3f}".format(rate))
        
        
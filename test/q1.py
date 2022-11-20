class Match:
    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2

    def findWinner(self) -> str:
        c1 = self.special(self.player1)
        c2 = self.special(self.player2)

        if c1 > c2:
            return 'Player1'
        elif c1 < c2:
            raise OutException("Player 1 out")
        else:
            raise WicketOutException("ALL OUT")

    def special(self, arr):
        c = 0
        for i in range(len(arr) - 2):
            if not arr[i] % 2 and not arr[i + 1] % 2 and not arr[i + 1] % 2:
                c += 1
        return c


class WicketOutException(Exception):
    def __init__(self, message):
        self.message = message


class OutException(Exception):
    def __init__(self, message):
        self.message = message











p1 = [2, 2, 4, 6]
p2 = [2, 2, 6, 8]
d = Match(p1, p2)

try:
    d.findWinner()
except Exception as e:
    print(e.message)


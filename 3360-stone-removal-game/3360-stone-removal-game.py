class Solution:
    def canAliceWin(self, n: int) -> bool:
        move = 10
        alice_turn = True
        while n >= move:
            n -= move
            move -= 1
            alice_turn = not alice_turn
        return not alice_turn
#Welcome to Robert Tang Wu version of tic-tac-toe Game- Object Oriented

#  00 01 02 03
#  04 05 06 07
#  08 09 10 11


class Board:
#set up the winning combos and the board
    winning_row_combos = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
    winning_col_combos = [[0,4,8],[1,5,9],[2,6,10],[3,7,11],[0,5,10],[1,6,11],[2,5,8],[3,6,9]]
    board = ["-"] * 12
# display the baord in this way
    def display(self):
        print
        print("~" * 15)
        print(" "+ self.board[0]+ " | " + self.board[1]+ " | " + self.board[2]+ " | " +self.board[3]+ " ")
        print(" " * 15)
        print(" "+self.board[4]+ " T " + self.board[5]+ " T " +self.board[6]+ " T " +self.board[7]+ " ")
        print(" " * 15)
        print(" "+self.board[8]+ " | " + self.board[9]+ " | " + self.board[10]+ " | " +self.board[11]+ " ")
        print("~" * 15)

 
    
    def winner(self):
  # check the board if the player has win the game      
        for  row_combo in self.winning_row_combos:
            if self.board[row_combo[0]] == self.board[row_combo[1]] == self.board[row_combo[2]] == self.board[row_combo[3]]!= "-":
                return self.board[row_combo[0]]
        
        for col_combo in self.winning_col_combos:
            if self.board[col_combo[0]] == self.board[col_combo[1]] == self.board[col_combo[2]] != "-":
                return self.board[col_combo[0]]
          # check draw when board is full
        if "-" not in self.board:
            return "Draw"
        return None
    
    # where the number have been input already then will block the player to input the same number
    def is_valid_move(self, position):
        return 0 <= position < 12 and self.board[position] == "-"
        

    def make_move(self, position, symbol):
        if self.is_valid_move(position):
            self.board[position] = symbol
            return True
        return print("Invalid move. Try again.")
    
    
class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self):
        # This part I have use f function instead using .format() because this way can help me write less code
        while True:
            # Here I use while loop and try except method 
            # to tracking the player each input not just check one time
            try:
                position = int(input(f"Player {self.symbol}'s turn. Enter your move (1-12): "))-1
                # Only allow the player to input 1 to 12 
                # if input other number of letter will ask them to input again
                if 1<= position + 1 <=12 :
                    return position
                else: 
                    print("Invalid input. Please enter a number between 1 and 12.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 12.")




class Game:
    def __init__(self):
        self.board = Board()
        # R mean Robert and W mean Tang Wu and add together is my full name Robert Tang Wu
        self.players = [Player("R"), Player("W")]
        #set the current is R
        self.current_player = self.players[0]

    def switch_players(self):
        #here is the method that use to switch the player
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def play_game(self):
        #21370916 is my student ID
        print("Welcome to the version 21370916 tic-tac-toe game")
        while True:
            self.board.display()
            position = self.current_player.make_move()
            if self.board.make_move(position, self.current_player.symbol):
                check_winner = Board.winner(self.board)
                if check_winner:
                    self.board.display()
                    if check_winner == "Draw":
                        print("Game Draw!")
                    else:
                        # This part I have use f function instead using .format() because this way can help me write less code
                        print(f"Player {check_winner} wins!")
                    break
                self.switch_players()
                
                
def main():
      # run the main game 
    game =Game()
    game.play_game()

if __name__ == "__main__":
    main()

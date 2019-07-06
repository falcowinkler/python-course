class GuessingGame:
    
    def __init__(self, geheime_zahl):
        self.lives = 10
        self.geheime_zahl = geheime_zahl
    
    def guess(self, number):
        if self.geheime_zahl != number:
            self.lives -= 1
            
        if self.geheime_zahl > number:
            return -1
        elif self.geheime_zahl < number:
            return 1
        else:
            return 0
    
    def is_game_over(self):
        return self.lives <= 0
    
game = GuessingGame(42)
while True:
    user_input = input("Bitte Zahl eingeben: ")
    result = game.guess(int(user_input))
    if result == -1:
        print("Zu klein")
    elif result == 1:
        print("Zu groß")
    else:
        print("Richtig")
    if game.is_game_over():
        print("Game Over")
    
            
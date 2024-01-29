import random


class Player:
    def __init__(self, player_id, start_rating=0):
        self.player_id = player_id
        self.rating = start_rating
        self.participations = []

    def update_rating(self, points):
        self.rating += points


class Tournament:
    def __init__(self, tournament_id):
        self.tournament_id = tournament_id
        self.players = []
        self.group_results = []
        self.bracket_results = []

    def add_player(self, player):
        self.players.append(player)

    def play_group_stage(self):
        # Логика для проведения группового этапа
        # Обновление рейтингов игроков
        for group in self.group_results:
            for game in group:
                game.play()
                game.winner.update_rating(3)  # Например, 3 балла за победу

    def play_bracket_stage(self):
        # Логика для проведения турнирной сетки
        # Обновление рейтингов игроков
        for game in self.bracket_results[0]:  # Берем первую (и единственную) турнирную сетку
            game.play()
            game.winner.update_rating(5)  # Например, 5 баллов за победу

    def simulate_tournament(self):
        self.play_group_stage()
        self.play_bracket_stage()

class Game:
    def __init__(self, player1, player2, winner=None):
        self.player1 = player1
        self.player2 = player2
        self.winner = winner

    def play(self):
        # Логика для проведения отдельной игры
        # Определение победителя и обновление рейтингов
        if random.choice([True, False]):  # Пример случайного выбора победителя
            self.winner = self.player1
        else:
            self.winner = self.player2


# Пример использования
if __name__ == "__main__":
    player1 = Player("Player1")
    player2 = Player("Player2")
    player3 = Player("Player3")
    player4 = Player("Player4")

    tournament = Tournament("Tournament1")
    tournament.add_player(player1)
    tournament.add_player(player2)
    tournament.add_player(player3)
    tournament.add_player(player4)

    # Групповой этап
    group1 = [Game(player1, player2), Game(player3, player4)]
    group2 = [Game(player1, player3), Game(player2, player4)]
    tournament.group_results = [group1, group2]

    # Турнирная сетка
    bracket1 = [Game(player1, player4), Game(player2, player3)]
    tournament.bracket_results = [bracket1]

    # Симулировать турнир
    tournament.simulate_tournament()

    # Получить отсортированный список игроков по рейтингу в порядке убывания
    sorted_players = sorted(tournament.players, key=lambda player: player.rating, reverse=True)

    # Информация о первом, втором и третьем местах
    print(f"Победитель турнира: {sorted_players[0].player_id} с {sorted_players[0].rating} баллами")
    print(f"Второе место: {sorted_players[1].player_id} с {sorted_players[1].rating} баллами")
    print(f"Третье место: {sorted_players[2].player_id} с {sorted_players[2].rating} баллами")


from abc import ABC, abstractmethod


class AttackStrategy(ABC):
    @abstractmethod
    def attack(self):
        pass


class LaserAttack(AttackStrategy):
    def attack(self):
        return "Атака лазером!"


class WeaponAttack(AttackStrategy):
    def attack(self):
        return "Атака оружием!"


class CombinedAttack(AttackStrategy):
    def attack(self):
        return "Кинуть кирпич!"


class MediaNotification(ABC):
    @abstractmethod
    def notify(self, city: str, result: str):
        pass


class NewspaperNotification(MediaNotification):
    def notify(self, city: str, result: str, villain: str):
        return (f"Специальное издание газеты в {city}:\nГород в безопасности! "
                f"Герой победил {villain} приемом {result}")


class TVNotification(MediaNotification):
    def notify(self, city: str, result: str, villain: str):
        return (f"Экстренный выпуск новостей по TV в {city}:\nГород в безопасности! "
                f"Герой победил {villain} приемом {result}")


class AntagonistPool:
    def __init__(self):
        self.antagonists = {}

    def add_antagonist(self, city: str, antagonist: str):
        self.antagonists[city] = antagonist

    def get_antagonist(self, city: str):
        return self.antagonists.get(city)


class Superhero:
    def __init__(
            self,
            attack_strategy: AttackStrategy,
            city: str,
            media_notification: MediaNotification,
            antagonist_pool: AntagonistPool
    ):
        (
            self.attack_strategy,
            self.city,
            self.media_notification,
            self.antagonist_pool
        ) = attack_strategy, city, media_notification, antagonist_pool

    def save_city(self):
        antagonist = self.antagonist_pool.get_antagonist(self.city)
        attack_result = self.attack_strategy.attack()
        print(f"{self.city} в опасности от {antagonist}!"
              f"\nГерой использует - {attack_result}\nХорошее попадание и это - Победа над злом!")
        villain_name = f"{antagonist}"
        print(self.media_notification.notify(self.city, attack_result, villain_name))


if __name__ == "__main__":

    antagonist_pool = AntagonistPool()
    antagonist_pool.add_antagonist("Токио", "Годзилла")
    antagonist_pool.add_antagonist("Кострома", "Киборг-убийца")
    antagonist_pool.add_antagonist("Готэм", "Джокер")

    godzilla = Superhero(LaserAttack(), "Токио", TVNotification(), antagonist_pool)
    kiborg = Superhero(WeaponAttack(), "Кострома", NewspaperNotification(), antagonist_pool)
    joker = Superhero(CombinedAttack(), "Готэм", TVNotification(), antagonist_pool)

    godzilla.save_city()
    kiborg.save_city()
    joker.save_city()


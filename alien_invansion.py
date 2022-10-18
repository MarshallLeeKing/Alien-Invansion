
# Создание окна Pygame и обработка ввода
import sys
import pygame
from settings import Settings


class AlienInvansion:
    # Класс для управления ресурсами игры
    def __init__(self) -> None:
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invansion")
        self.bg_color = (230, 230, 230)

    def run_game(self):
        # Запуск основного цикла игры
        while True:
            # Отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Заполняем экран цветом bg_color
            self.screen.fill(self.settings.bg_color)

            # Отображение последнего прорисованного экрана
            pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    ai = AlienInvansion()
    ai.run_game()

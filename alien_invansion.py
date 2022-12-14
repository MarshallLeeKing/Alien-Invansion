
# Создание окна Pygame и обработка ввода
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvansion:
    # Класс для управления ресурсами игры
    def __init__(self) -> None:

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invansion")
        self.bg_color = (230, 230, 230)

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

    def run_game(self):
        # Запуск основного цикла игры
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):

        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # Заполняем экран цветом bg_color
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

    def _fire_bullet(self):
        # Создание снаряда и включение его в группу Bullets
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # обновляем позиции снарядов и очищаем лишние
        self.bullets.update()

        # Удаление лишних снарядов
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    ai = AlienInvansion()
    ai.run_game()

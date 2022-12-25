
# модуль для работы с объектом корабля
import pygame


class Ship():

    def __init__(self, ai_game) -> None:
        # Инициализация корабля и задание его начальной позиции
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загружаем изображение корабля и получаем прямоугольник
        self.image = pygame.image.load('Alien Invansion/img/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохраняем координату корабля
        self.x = float(self.rect.x)

        # Флаг перемещения корабля вправо
        self.moving_right = False
        # Флаг перемещения корабля влево
        self.moving_left = False

    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        # Отрисовка корабля в текущей позиции
        self.screen.blit(self.image, self.rect)

import arcade

NORMAL_IMG = ':resources:gui_basic_assets/red_button_normal.png'
PRESSED_IMG = ':resources:gui_basic_assets/red_button_press.png'
NORMAL = 0
PRESSED = 1


class Button(arcade.Sprite):
    """Класс кнопки"""

    def __init__(self, normal_img='', pressed_img='', scale=1):
        super().__init__(scale=scale)
        """
        normal_img: текстура кнопки в нормальном состоянии
        pressed_img: текстура кнопки в нажатом состоянии
        """
        if not normal_img:
            normal_img = NORMAL_IMG
        if not pressed_img:
            pressed_img = PRESSED_IMG
        self.textures = []
        self._load_textures(normal_img, pressed_img)

        self.status = NORMAL
        self._binded_function = None

    def _load_textures(self, normal_img, pressed_img):
        """Загружает текстуры кнопки из файлов ресурсов"""
        texture = arcade.load_texture(normal_img)
        self.textures.append(texture)
        texture = arcade.load_texture(pressed_img)
        self.textures.append(texture)

    def on_mousse_press(self, x: float, y: float, button: int, modifiers: int):
        """Обработчик нажатия на кнопку"""
        if self.collides_with_point((x, y)):
            self.status = PRESSED
            if self._binded_function:
                self._binded_function()

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        """Обработчик отпускания кнопки мыши"""
        self.status = NORMAL

    def bind(self, function):
        """Привязывает функцию или метод к кнопке"""
        self._binded_function = function

    def update(self):
        self.texture = self.textures[self.status]


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.WHITE_SMOKE
        self.button = Button(scale=0.5)
        self.button.center_x = 100
        self.button.center_y = 100
        self.button.bind(arcade.exit)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.button.on_mousse_press(x, y, button, modifiers)

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        self.button.on_mouse_release(x, y, button, modifiers)

    def update(self, delta_time: float):
        self.button.update()

    def on_draw(self):
        arcade.start_render()
        self.button.draw()


if __name__ == '__main__':
    app = MyGame()
    app.run()

class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_colour):
        super().__init__()
        """Initialize button with some parametrs

        :param image: button background
        :param pos: button position on screen
        :param text_input: text of a button
        :param font: font of rendered text
        :param base_color: color without mouse hovering
        :param hovering_colour: color with mouse hover
        """
        self.image = image
        self.posx = pos[0]
        self.posy = pos[1]
        self.text_input = text_input
        self.font = font
        self.base_color = base_color  # without hovering
        self.hover_colour = hovering_colour  # with hovering
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.posx, self.posy))
        self.text_rect = self.text.get_rect(center=(self.posx, self.posy))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_events(self, pos):
        """Allows Button to check if it's being pressed or not

        :param pos: mouse coordinates on screen
        :return bool: True or False
        """
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(
            self.rect.top, self.rect.bottom
        ):
            return True
        return False

    def colorwheel(self, pos):
        """allows Button to change color based on mouse coordinates

        :param pos: mouse coordinates on screen
        """
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(
            self.rect.top, self.rect.bottom
        ):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

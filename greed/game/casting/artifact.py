from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
import random
# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """set properties for an artifact."""
    def __init__(self):
        # carries over actor attributes
        super().__init__()
    
    def set_message(self, msg):
        """Sets the self.message attribute."""
        self._message = msg

    def get_message(self):
        """Returns self.message."""
        return self._message

    def create_artifacts(self, cast, number, COLS = 60, CELL_SIZE = 15, FONT_SIZE = 15):
        """Creates a number of artifacts at the top of the screen.
        Args:
            cast (Class): the cast lets us add new actors.
            number (int): the number of artifacts there should be total on the screen.
            COLS ()

        """
        if len(cast.get_actors("artifacts")) < number:
            text = random.choice(["O", "*"])
            if text == "*":
                message = 1
            else: message = -1

            # finds random x value from 1 to the column max
            x = random.randint(1, COLS - 1)
            y = random.randint(-50, 1)
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)
            artifact.set_message(message)
            artifact.set_speed()
            cast.add_actor("artifacts", artifact)
        
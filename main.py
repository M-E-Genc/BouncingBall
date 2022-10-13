"""
Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Bouncing Ball"

x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 4 * 3

# velocity should be between 3 and 35, over 35 leaves the screen, below 3 does not jump
bouncing_velocity = 30

# Movement speed of player, in pixels per frame
GRAVITY = 1


class BouncingBall(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the ball sprite
        self.ball_sprite = None
        self.ground = None

        # Our physics engine
        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Initialize Scene
        self.scene = arcade.Scene()

        # Set up the ball, specifically placing it at these coordinates.
        self.ball_sprite = arcade.SpriteCircle(10, arcade.color.CADMIUM_RED)
        self.ball_sprite.center_x = x
        self.ball_sprite.center_y = y
        self.scene.add_sprite("Ball", self.ball_sprite)

        # Create the ground
        self.ground = arcade.SpriteSolidColor(SCREEN_WIDTH, 10, arcade.color.GREEN)
        self.ground.center_x = x
        self.ground.center_y = 32
        self.scene.add_sprite("Ground", self.ground)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.ball_sprite, gravity_constant=GRAVITY, walls=self.scene["Ground"]
        )

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw the Scene
        self.scene.draw()

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the ball with the physics engine
        self.physics_engine.update()

        # Check if the ball hits the ground and bounce it back with the given velocity
        if self.ball_sprite.collides_with_point((x, 38)):
            self.ball_sprite.change_y = bouncing_velocity


def main():
    """Main function"""
    window = BouncingBall()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

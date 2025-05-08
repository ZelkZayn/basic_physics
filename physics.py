import pygame 
import random
import math

# Basic Intiliaization
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
debounce = False

# Constants
gravity_constant = 9.8
radius = 30

# Circle class group
class Circle(pygame.sprite.Sprite):
    # __init__ method is used in order to intialize a object, made using the class in python. It accepts the arguements that are passed in through as your creating a new object with
    # the class.
    def __init__(self, position):
        # Intializes the Spirite, so it can handle things such as updating and adding will work
        super().__init__()
        # Creates a surface for the circle to be drawn onto
        # pygame.SRCALPHA, creates a transparent background, so any pixels i don't fill in are transparent
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        # random colour
        rgb_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        # drawing the circle onto the surface
        pygame.draw.circle(self.image, rgb_color,(radius, radius), radius)
        # creates a rectangle at the position in the 
        self.rect = self.image.get_rect(center = position)
        self.velocity = pygame.math.Vector2(0,0)
        self.pos = pygame.math.Vector2(position)
        self.radius = radius


    def update_gravity(self, dt):
        self.rect.move_ip(self.velocity)
        self.velocity.y += gravity_constant * dt
        self.pos.y += gravity_constant * dt

        if self.velocity.y > 0 and self.rect.colliderect(target):
            self.rect.bottom = target.top
            # Makes sure that the ball loses some velocity
            if abs(self.velocity.y) >= 2.0:
                self.velocity.y *= -0.9
            else:
                self.velocity.y = 0
        

def circle_collision(c1, c2):
    normal_line = (c2.pos.y - c1.pos.y) / abs(c2.pos.x - c1.pos.x)
    
    return 




# Group to hold all the spirites
spirite_group = pygame.sprite.Group()



while running:
    # Checks if the user clicks the x button to get rid of the screen, need this otherwise it wont work
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False         

    # checks if the user presses the left mouse button
    mouse_one = pygame.mouse.get_pressed()[0]
    mouse_one_pressed = pygame.mouse.get_pressed()[0]
    
    # if the user does click the left mouse button, then it gets the current mouses position
    if mouse_one and not debounce:
        mouse_pos = pygame.mouse.get_pos()
        # creates a circle at the mouse position
        spirite_group.add(Circle(mouse_pos))
        debounce = True

    target = pygame.Rect(0, 660, 1280, 60)

    if not mouse_one_pressed:
        debounce = False

    collisions = pygame.sprite.groupcollide(
        spirite_group,
        spirite_group,
        False,
        False,
        collided=pygame.sprite.collide_circle
    )

    for circle, hit_list in collisions.items():
        for hit_circle in hit_list:
            if circle is not hit_circle:
                circle_collision(circle, hit_circle)




    for ball in spirite_group:
        ball.update_gravity(dt)
            

    screen.fill((255,255,255))
    pygame.draw.rect(screen, "green", target)
    spirite_group.draw(screen)
    pygame.display.flip()

    dt = clock.tick(120) / 1000

    

pygame.quit()


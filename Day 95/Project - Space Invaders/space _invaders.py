import random
import turtle

wn = turtle.Screen()
wn.title("Space Invaders")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# SCORE
score = 0
write_score = turtle.Turtle()
write_score.penup()
write_score.hideturtle()
write_score.color("white")
write_score.goto(240, 250)

write_score.write(f"Score:{score}", font=('Arial', 14, 'normal'))

# PLAYER
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.goto(0, -250)
player.setheading(90)

player_speed = 20

# BULLET
bullet = turtle.Turtle()
bullet.turtlesize(.5)
bullet.shape("circle")
bullet.color("white")
bullet.penup()
bullet.hideturtle()

bullet_speed = 5
bullet_state = "ready"

# ENEMIES
enemies = []
for _ in range(12):
    enemy = turtle.Turtle()
    enemy.shape("square")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    enemy.goto(random.randint(-300, 300), random.randint(100, 250))
    enemies.append(enemy)

enemy_speed = 1
enemy_direction = 0.5


# FUNCTIONS
def move_left():
    x = player.xcor() - player_speed
    if x > -380:
        player.setx(x)


def move_right():
    x = player.xcor() + player_speed
    if x < 380:
        player.setx(x)


def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.showturtle()
        bullet.goto(player.xcor(), player.ycor() + 15)
        bullet.showturtle()


def is_collision(t1, t2):
    return t1.distance(t2) < 20


# CONTROLS
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")





while True:
    wn.update()

    # move bullet
    if bullet_state == "fire":
        bullet.sety(bullet.ycor() + bullet_speed)

        if bullet.ycor() > 290:
            bullet.hideturtle()
            bullet_state = "ready"

    # move enemies
    for enemy in enemies:
        y = enemy.ycor()
        y += -0.5
        enemy.sety(y)

        # bullet hit enemy
        if bullet_state == "fire" and is_collision(bullet, enemy):
            write_score.clear()
            score += 1
            write_score.write(f"Score:{score}", font=('Arial', 14, 'normal'))
            bullet.hideturtle()
            bullet_state = "ready"
            enemy.goto(random.randint(-300, 300), random.randint(100, 250))

        #  respawn enemy
        if enemy.ycor() < -250:
            enemy.goto(random.randint(-300, 300), random.randint(200, 290))

        # game over
        if is_collision(enemy, player):
            print("GAME OVER")
            exit()

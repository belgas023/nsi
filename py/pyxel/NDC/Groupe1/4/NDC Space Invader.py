import pyxel
import random

pyxel.init(128, 128)
pyxel.load("3.pyxres")
pyxel.playm(0, tick=0, loop=True)

def reset():
    global ship_x, ship_y, bullets, enemies, score, frame_count, game_over, start, shoot_cooldown, lives
    ship_x = 62
    ship_y = 100
    bullets = []
    enemies = []
    score = 0
    frame_count = 0
    game_over = False
    start = True 
    shoot_cooldown = 0
    lives = 5

def update():
    global frame_count, shoot_cooldown, game_over, start, ship_x, bullets, enemies, score, lives
    if start:
        if pyxel.btnp(pyxel.KEY_R):
            start = False
        return

    if game_over:
        if pyxel.btnp(pyxel.KEY_R):
            reset()
        return

    frame_count += 1

    if shoot_cooldown > 0:
        shoot_cooldown -= 1

    if pyxel.btn(pyxel.KEY_LEFT):
        ship_x = max(ship_x - 2, 0)
    if pyxel.btn(pyxel.KEY_RIGHT):
        ship_x = min(ship_x + 2, 120)

    if pyxel.btn(pyxel.KEY_SPACE) and shoot_cooldown == 0:
        bullets.append((ship_x + 3, ship_y))
        shoot_cooldown = 10

    bullets[:] = [(x, y - 4) for x, y in bullets if y > 0]

    if frame_count % 30 == 0:
        enemies.append((random.randint(10, 110), 0))

    new_enemies = []
    for ex, ey in enemies:
        if score < 30:
            ey += 1
        elif score >= 30:
            ey += 2

        if abs(ex - ship_x) < 8 and abs(ey - ship_y) < 8:
            lives -= 1
            if lives <= 0:
                game_over = True
            continue

        if ey > 128:
            lives -= 1
            if lives <= 0:
                game_over = True
        else:
            new_enemies.append((ex, ey))

    enemies[:] = new_enemies

    new_bullets = []
    new_enemies = []

    for ex, ey in enemies:
        enemy_hit = False
        for i, (bx, by) in enumerate(bullets):
            if abs(bx - ex) < 8 and abs(by - ey) < 8:
                score += 1
                enemy_hit = True
                bullets.pop(i)
                break
        if not enemy_hit:
            new_enemies.append((ex, ey))

    enemies[:] = new_enemies

def draw():
    if score < 30:
        pyxel.cls(0)
    if score >= 30:
        pyxel.cls(1)

    if score < 30:
        if pyxel.btn(pyxel.KEY_RIGHT):
            pyxel.blt(ship_x, ship_y, 0, 117, 32, 7, 16, 1)
        elif pyxel.btn(pyxel.KEY_LEFT):
            pyxel.blt(ship_x-4, ship_y, 0, 132, 32, 7, 16, 1)
        else:
            pyxel.blt(ship_x-4, ship_y, 0, 82, 32, 12, 16, 1)
    elif score >= 30:
        if pyxel.btn(pyxel.KEY_RIGHT):
            pyxel.blt(ship_x-4, ship_y, 0, 117, 16, 7, 16, 1)
        elif pyxel.btn(pyxel.KEY_LEFT):
            pyxel.blt(ship_x-4, ship_y, 0, 132, 16, 7, 16, 1)
        else:
            pyxel.blt(ship_x-4, ship_y, 0, 82, 16, 12, 16, 1)

    if pyxel.frame_count % 16 == 1 and game_over == False:
        pyxel.blt(random.randint(0, 128), random.randint(0, 128), 0, 6, 85, 5, 5, 1)
    if pyxel.frame_count % 16 == 3 and game_over == False:
        pyxel.blt(random.randint(0, 128), random.randint(0, 128), 0, 6, 85, 5, 5, 1)
    if pyxel.frame_count % 16 == 5 and game_over == False:
        pyxel.blt(random.randint(0, 128), random.randint(0, 128), 0, 6, 85, 5, 5, 1)
    if pyxel.frame_count % 16 == 7 and game_over == False:
        pyxel.blt(random.randint(0, 128), random.randint(0, 128), 0, 6, 85, 5, 5, 1)
    if pyxel.frame_count % 16 == 9 and game_over == False:
        pyxel.blt(random.randint(0, 128), random.randint(0, 128), 0, 6, 85, 5, 5, 1)
    if pyxel.frame_count % 16 == 11 and game_over == False:
        pyxel.blt(random.randint(0, 128), random.randint(0, 128), 0, 6, 85, 5, 5, 1)
    if pyxel.frame_count % 16 == 13 and game_over == False:
        pyxel.blt(random.randint(0, 128), random.randint(0, 128), 0, 6, 85, 5, 5, 1)
    if pyxel.frame_count % 16 == 15 and game_over == False:
        pyxel.blt(random.randint(0, 128), random.randint(0, 128), 0, 6, 85, 5, 5, 1)

    if game_over:
        pyxel.text(45, 50, "GAME OVER", 8)
        pyxel.text(15, 60, "Appuie sur R pour rejouer", 7)
        pyxel.text(45, 70, f"Score: {score}", 7)
        return
    if start:
        pyxel.text(20, 50, "Appuie sur R pour jouer", 7)


    for x, y in bullets:
        if score < 30:
            pyxel.blt(x-4, y, 0, 33, 64, 6, 6, 1)
        if score >= 30:
            pyxel.blt(x-4, y, 0, 41, 64, 6, 8, 1)

    for x, y in enemies:
        pyxel.blt(x - 4, y - 4, 0, 49, 50, 14, 11, 1)

    pyxel.text(5, 5, f"Score: {score}", 7)
    pyxel.text(5, 15, f"Vies: {lives}", 8)

reset()
pyxel.run(update, draw)


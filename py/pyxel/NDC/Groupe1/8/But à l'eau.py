import pyxel
import random

pyxel.init(128, 128, "But à l'eau", fps=20, quit_key=pyxel.KEY_BACKSPACE)
pyxel.load("theme.pyxres")

game = {"phase": 0, "team0": 0, "team1": 0}
teams = [
    (0, 0, "France"), (0, 16, "Espagne"), (0, 32, "Italie"), (0, 48, "Bresil"),
    (16, 0, "Angleterre"), (16, 16, "Portugal"), (16, 32, "Argentine"), (16, 48, "Algerie"),
    (32, 0, "Maroc"), (32, 16, "Australie"), (32, 32, "Allemagne"), (32, 48, "Coree.S"),
    (48, 0, "Suede"), (48, 16, "Japon"), (48, 32, "Nigeria"), (48, 48, "Pays-Bas")
]
players = [[60, 30], [60, 90]]
bomb = [[0, 32], [60, 60], [0, 0]]
bomb_speed_x = 1.5
bomb_speed_y = 1.5

setup_time = 20
setup_timer = setup_time
time_match = 20 * 90

score_team0 = 0
score_team1 = 0
team0_lock = False
team1_lock = False

pyxel.mouse(False)

def update():
    global setup_timer, time_match, score_team0, score_team1, team0_lock, team1_lock
    global bomb_speed_x, bomb_speed_y

    if game["phase"] == 0:
        if pyxel.btnp(pyxel.KEY_RETURN):
            game["phase"] = 1
        return

    if game["phase"] == 1:
        if team0_lock and team1_lock:
            game["phase"] = 2
            setup_timer = setup_time

        if pyxel.btnp(pyxel.KEY_RETURN):
            team1_lock = not team1_lock
        if pyxel.btnp(pyxel.KEY_TAB):
            team0_lock = not team0_lock
        if pyxel.btnp(pyxel.KEY_RIGHT) and not team1_lock:
            game["team1"] = (game["team1"] + 1) % 16
        elif pyxel.btnp(pyxel.KEY_LEFT) and not team1_lock:
            game["team1"] = (game["team1"] - 1) % 16
        if pyxel.btnp(pyxel.KEY_Q) and not team0_lock:
            game["team0"] = (game["team0"] - 1) % 16
        elif pyxel.btnp(pyxel.KEY_D) and not team0_lock:
            game["team0"] = (game["team0"] + 1) % 16

    elif game["phase"] == 2:
        setup_timer -= 1
        if setup_timer <= 0:
            game["phase"] = 3

    elif game["phase"] == 3:
        time_match -= 1
        if time_match <= 0:
            game["phase"] = 4

        # Joueurs
        if pyxel.btn(pyxel.KEY_Z) and players[0][1] > 24:
            players[0][1] -= 1
        if pyxel.btn(pyxel.KEY_S) and players[0][1] < 128 - 32:
            players[0][1] += 1
        if pyxel.btn(pyxel.KEY_D) and players[0][0] < 128 - 16:
            players[0][0] += 1
        if pyxel.btn(pyxel.KEY_Q) and players[0][0] > 8:
            players[0][0] -= 1

        if pyxel.btn(pyxel.KEY_UP) and players[1][1] > 24:
            players[1][1] -= 1
        if pyxel.btn(pyxel.KEY_DOWN) and players[1][1] < 128 - 32:
            players[1][1] += 1
        if pyxel.btn(pyxel.KEY_RIGHT) and players[1][0] < 128 - 16:
            players[1][0] += 1
        if pyxel.btn(pyxel.KEY_LEFT) and players[1][0] > 8:
            players[1][0] -= 1

        # Déplacement bombe
        bomb[1][0] += bomb_speed_x
        bomb[1][1] += bomb_speed_y

        # Rebonds murs
        if bomb[1][0] <= 8 or bomb[1][0] >= 128 - 16:
            bomb_speed_x = -bomb_speed_x
        if bomb[1][1] <= 24 or bomb[1][1] >= 128 - 32:
            bomb_speed_y = -bomb_speed_y

        # Collision joueurs
        if collision():
            bomb_speed_x = -bomb_speed_x

        # But équipe 1 en haut
        if 56 <= bomb[1][0] <= 72 and bomb[1][1] <= 24:
            score_team1 += 1
            reset_ball()

        # But équipe 0 en bas
        if 56 <= bomb[1][0] <= 72 and bomb[1][1] >= 159:
            score_team0 += 1
            reset_ball()

    elif game["phase"] == 4:
        if score_team0 > score_team1:
             winner = team0_lock
        elif score_team0 < score_team1:
            winner = team1_lock 
        
        if pyxel.btnp(pyxel.KEY_RETURN):
            reset_game()

def collision():
    for player in players:
        if (bomb[1][0] + 8 > player[0] and bomb[1][0] < player[0] + 8 and
            bomb[1][1] + 8 > player[1] and bomb[1][1] < player[1] + 8):
            return True
    return False

def reset_game():
    global players, bomb, team0_lock, team1_lock, time_match, score_team0, score_team1
    global bomb_speed_x, bomb_speed_y

    game["phase"] = 0
    players = [[16, 58], [112, 58]]
    bomb[1] = [60, 60]
    bomb_speed_x = random.choice([-1.5, 1.5])
    bomb_speed_y = random.choice([-1.5, 1.5])
    team0_lock = False
    team1_lock = False
    time_match = 20 * 90
    score_team0 = 0
    score_team1 = 0

def reset_ball():
    global bomb, bomb_speed_x, bomb_speed_y
    bomb[1] = [60, 60]
    bomb_speed_x = random.choice([-1.5, 1.5])
    bomb_speed_y = random.choice([-1.5, 1.5])

def draw():
    pyxel.cls(0)

    if game["phase"] == 0:
        pyxel.text(15, 30, "Bienvenue dans Fifake 2025", 11)
        pyxel.text(15, 50, "ZQSD : J1 | Fleches : J2", 7)
        pyxel.text(0, 65, "Appuie sur ENTREE pour commencer", 10)

    elif game["phase"] == 1:
        pyxel.text(32, 30, "Choix des equipes", 3)
        pyxel.text(10, 80, teams[game['team0']][2], 10)
        pyxel.text(75, 80, teams[game['team1']][2], 10)
        pyxel.blt(16, 56, 0, teams[game['team0']][0], teams[game['team0']][1], 16, 16, 14)
        pyxel.blt(98, 56, 0, teams[game['team1']][0], teams[game['team1']][1], 16, 16, 14)

    elif game["phase"] == 2:
        pyxel.text(60, 30, str(setup_timer // 20), 3)
        pyxel.text(10, 80, teams[game['team0']][2], 10)
        pyxel.text(75, 80, teams[game['team1']][2], 10)

    elif game["phase"] == 3:
        pyxel.blt(0, 16, 0, 0, 80, 128, 112)
        pyxel.text(16, 2, teams[game['team0']][2], 10)
        pyxel.text(76, 2, teams[game['team1']][2], 10)
        pyxel.text(32, 10, str(score_team0), 3)
        pyxel.text(92, 10, str(score_team1), 3)
        pyxel.text(62, 10, str(time_match // 20), 3)

        pyxel.blt(int(players[0][0]), int(players[0][1]), 1, teams[game['team0']][0] // 2, teams[game['team0']][1] // 2, 8, 8, 14)
        pyxel.blt(int(players[1][0]), int(players[1][1]), 1, teams[game['team1']][0] // 2, teams[game['team1']][1] // 2, -8, 8, 14)
        pyxel.blt(int(bomb[1][0]), int(bomb[1][1]), 1, 0, 32, 8, 8, 14)
        
        
            

        # Dessiner les cages
        for x in range(56, 73):
            pyxel.pset(x, 24, 7)
            pyxel.pset(x, 128-25, 7)

    elif game["phase"] == 4:
        pyxel.text(16, 2, teams[game['team0']][2], 10)
        pyxel.text(76, 2, teams[game['team1']][2], 10)
        pyxel.text(32, 10, str(score_team0), 3)
        pyxel.text(92, 10, str(score_team1), 3)
        #if score_team0 > score_team1:
            
        pyxel.text(40, 50, "FIN DU MATCH", 8)
        pyxel.text(5, 65, "Appuie sur ENTREE pour rejouer", 7)

pyxel.run(update, draw)
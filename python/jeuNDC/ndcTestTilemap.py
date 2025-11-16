import pyxel


tailleCase = 8
pyxel.init(23*tailleCase, 14*tailleCase, title="test", fps=30)
pyxel.load('4.pyxres')

def update():
    pass


def draw():
    pyxel.bltm(0, 0, 0, 0, 15, 15, 15, pyxel.COLOR_BLACK)

pyxel.run(update, draw)
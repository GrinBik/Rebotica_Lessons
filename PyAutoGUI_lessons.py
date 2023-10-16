import pyautogui as gui
from time import sleep as sl


def show_pos():
    while True:
        print(gui.position())
        sl(2)


def spam():
    for i in range(10):
        gui.write("Hello")
        sl(0.05)
        gui.press('Enter')


def run():
    while True:
        gui.press('w', presses=3)
        sl(0.05)
    gui.keyDown('w')
    gui.keyUp('w')


# show_pos()

# gui.click(x=147, y=321, button='left')


# for i in range(2):
#     gui.click(x = 147, y = 321, button = 'left')
#     sl(0.005)

# gui.doubleClick(x = 147, y = 321, button = 'left')
# sl(4)
#
# sl(1)
# gui.moveTo(x=545, y=345)
# sl(1)
# gui.dragTo(x=390, y=660)
# sl(1)
# gui.dragTo(x=700, y=660)
# sl(1)
# gui.dragTo(x=545, y=345)
# sl(1)
#
# for i in range(1, 4, 1):
#     sl(1)
#     gui.moveTo(x=545 + 100*i, y=345)
#     sl(1)
#     gui.dragTo(x=390 + 100*i, y=660)
#     sl(1)
#     gui.dragTo(x=700 + 100*i, y=660)
#     sl(1)
#     gui.dragTo(x=545 + 100*i, y=345)
#     sl(1)

spam()

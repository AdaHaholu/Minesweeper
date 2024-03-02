import proximity as prox
import PySimpleGUI as sg


def checkProximity(event, window, coordinates, row, col):
    dummy = prox.countMine(event, coordinates, row, col)
    proximity = []

    for i in dummy[0][0]:
        if isMine(i) == False:
            if window[i].get_text() != " " and window[i].get_text() != "!":
                if prox.countMine(i, coordinates, row, col)[1] == 0:
                    proximity.append(i)

    for j in dummy[0][0]:
        if j not in proximity:
            if isMine(j) == False:
                updateButtonColor(j, window, coordinates, row, col)
        if j in proximity:
            window[j].update(" ", button_color="#999999", disabled=True)

    for prx in proximity:
        window[prx].update(button_color="#999999", disabled=True)
        checkProximity(prx, window, coordinates, row, col)


def updateButtonColor(event, window, coordinates, row, col):
    x = prox.countMine(event, coordinates, row, col)[1]
    if x == 1:
        window[event].update(
            x, disabled_button_color=("blue", "#999999"), disabled=True
        )
    elif x == 2:
        window[event].update(
            x, disabled_button_color=("green", "#999999"), disabled=True
        )
    elif x == 3:
        window[event].update(x, disabled_button_color=("red", "#999999"), disabled=True)
    elif x == 4:
        window[event].update(
            x, disabled_button_color=("purple", "#999999"), disabled=True
        )
    elif x == 5:
        window[event].update(
            x, disabled_button_color=("black", "#999999"), disabled=True
        )
    elif x == 6:
        window[event].update(
            x, disabled_button_color=("gray", "#999999"), disabled=True
        )
    elif x == 7:
        window[event].update(
            x, disabled_button_color=("maroon", "#999999"), disabled=True
        )
    elif x == 8:
        window[event].update(
            x, disabled_button_color=("turquoise", "#999999"), disabled=True
        )


def showMine(window, coordinates):
    mines = []

    for mine in coordinates:
        if mine[2] == 1:
            mines.append(mine)

    for x in mines:
        window[x].update("X", disabled_button_color=("white", "black"), disabled=True)


def isMine(event):
    if event[2] == 1:
        return True
    else:
        return False


def isWin(window, coordinates, difficulty):
    count = 0

    for i in coordinates:
        if window[i].get_text() != "" and window[i].get_text() != "!":
            count += 1
    if count + difficulty == len(coordinates):
        return True
    else:
        return False

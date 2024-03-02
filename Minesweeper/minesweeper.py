import PySimpleGUI as sg
import proximity as prox
import clickEvent as click
import layout as lyt
import keyboard as key


def minesweeper(row, col, difficulty):
    key.get_hotkey_name()
    coordinates = lyt.placeMine(row, col, difficulty)
    layout = [lyt.fCounter(difficulty)]
    layout.append(lyt.gridLayout(col, coordinates))
    layout.append(
        [
            sg.Button("Select Difficulty", key="dif", pad=(1, 1), use_ttk_buttons=True),
            sg.Button("Reset Board", key="res", pad=(1, 1), use_ttk_buttons=True),
        ]
    )

    window = sg.Window("Minesweeper", layout, element_justification="c")

    loop = True

    while loop:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            loop = False

        elif event == "res":
            window.close()
            minesweeper(row, col, difficulty)

        elif event == "dif":
            window.close()
            start()

        elif type(event) is tuple and key.is_pressed("shift") == True:
            if window[event].get_text() == "!":
                window[event].update("")
                window["fCount"].update(int(window["fCount"].get_text()) + 1)
            else:
                window[event].update("!", button_color=("red", ""))
                window["fCount"].update(int(window["fCount"].get_text()) - 1)

        elif click.isMine(event) == True:
            for i in coordinates:
                window[i].update(disabled=True)
            lyt.gameOver(window, coordinates, 0)
        elif click.isMine(event) == False:
            if window[event].get_text() == "!":
                window["fCount"].update(int(window["fCount"].get_text()) + 1)
            if prox.countMine(event, coordinates, row, col)[1] > 0:
                click.updateButtonColor(event, window, coordinates, row, col)
                if click.isWin(window, coordinates, difficulty) == True:
                    click.updateButtonColor(event, window, coordinates, row, col)
                    lyt.gameOver(window, coordinates, 1)
            else:
                window[event].update(" ", button_color="#999999", disabled=True)
                click.checkProximity(event, window, coordinates, row, col)
                if click.isWin(window, coordinates, difficulty) == True:
                    click.updateButtonColor(event, window, coordinates, row, col)
                    lyt.gameOver(window, coordinates, 1)


def start():
    layout = [
        [sg.Text("Choose Difficulty", key="text")],
        [
            sg.Button("Beginner", key="beg", size=(10, 1), use_ttk_buttons=True),
            sg.Button("Intermediate", key="int", size=(10, 1), use_ttk_buttons=True),
            sg.Button("Expert", key="exp", size=(10, 1), use_ttk_buttons=True),
        ],
    ]

    window = sg.Window("Difficulty", layout, element_justification="c")

    loop = True

    while loop:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            loop = False

        elif event == "beg":
            window.close()
            minesweeper(9, 9, 10)

        elif event == "int":
            window.close()
            minesweeper(16, 16, 40)

        elif event == "exp":
            window.close()
            minesweeper(16, 40, 99)


start()

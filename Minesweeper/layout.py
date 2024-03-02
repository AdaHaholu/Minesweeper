import random as rand
import PySimpleGUI as sg
import clickEvent as click


def placeMine(row, col, difficulty):
    coordinates = []
    for i in range(row):
        for j in range(col):
            coordinates.append((i, j))

    mines = rand.sample(range(0, row * col), difficulty)

    for i in mines:
        coordinates[i] = coordinates[i] + (1,)

    for crd in range(len(coordinates)):
        if len(coordinates[crd]) == 2:
            coordinates[crd] = coordinates[crd] + (0,)

    count = 0
    layout = []

    return coordinates


def gridLayout(col, coordinates):
    count = 0
    layout = []

    for i in range(col - 1, len(coordinates), col):
        buttons = []
        for crd in coordinates[(count) * col : i + 1]:
            buttons.append(
                sg.Button(
                    "",
                    size=(2, 1),
                    key=crd,
                    pad=(0, 0),
                    use_ttk_buttons=True,
                    button_color="#bbbbbb",
                )
            )
        count += 1
        layout.append(buttons)

    return layout


def gameOver(window, coordinates, cond):
    if cond == 0:
        layout = [
            [sg.Text("You hit a Mine!")],
            [sg.Button("Return to Board", key="return", use_ttk_buttons=True)],
        ]
    if cond == 1:
        layout = [
            [sg.Text("You Found All Mines!")],
            [sg.Button("Return to Board", key="return", use_ttk_buttons=True)],
        ]

    gWindow = sg.Window("Play Again", layout, element_justification="c")

    loop = True

    while loop:
        event, values = gWindow.read()

        if event == sg.WINDOW_CLOSED:
            click.showMine(window, coordinates)
            gWindow.close()
            loop = False

        elif event == "return":
            gWindow.close()
            click.showMine(window, coordinates)
            loop = False


def fCounter(difficulty):
    counter = sg.Button(
        difficulty,
        key="fCount",
        size=(4, 1),
        use_ttk_buttons=True,
        disabled=True,
        disabled_button_color=("red", "black"),
    )
    return [counter]


def timer():
    """"""

def countMine(event, coordinates, row, col):
    proximity = []
    mineCount = 0

    if 0 < event[0] < (row - 1) and 0 < event[1] < (col - 1):
        proximity.append(
            [
                coordinates[coordinates.index(event) - (col + 1)],
                coordinates[coordinates.index(event) - col],
                coordinates[coordinates.index(event) - (col - 1)],
                coordinates[coordinates.index(event) - 1],
                coordinates[coordinates.index(event) + 1],
                coordinates[coordinates.index(event) + (col - 1)],
                coordinates[coordinates.index(event) + col],
                coordinates[coordinates.index(event) + (col + 1)],
            ]
        )
        for x in proximity:
            for index in x:
                if index[2] == 1:
                    mineCount += 1
        return proximity, mineCount

    elif event[0] == 0 and event[1] == 0:
        proximity.append(
            [
                coordinates[coordinates.index(event) + 1],
                coordinates[coordinates.index(event) + col],
                coordinates[coordinates.index(event) + (col + 1)],
            ]
        )
        for x in proximity:
            for index in x:
                if index[2] == 1:
                    mineCount += 1
        return proximity, mineCount

    elif event[0] == (row - 1) and event[1] == (col - 1):
        proximity.append(
            [
                coordinates[coordinates.index(event) - 1],
                coordinates[coordinates.index(event) - col],
                coordinates[coordinates.index(event) - (col + 1)],
            ]
        )
        for x in proximity:
            for index in x:
                if index[2] == 1:
                    mineCount += 1
        return proximity, mineCount

    elif event[0] == (row - 1) and event[1] == 0:
        proximity.append(
            [
                coordinates[coordinates.index(event) - col],
                coordinates[coordinates.index(event) - (col - 1)],
                coordinates[coordinates.index(event) + 1],
            ]
        )
        for x in proximity:
            for index in x:
                if index[2] == 1:
                    mineCount += 1
        return proximity, mineCount

    elif event[0] == 0 and event[1] == (col - 1):
        proximity.append(
            [
                coordinates[coordinates.index(event) - 1],
                coordinates[coordinates.index(event) + col],
                coordinates[coordinates.index(event) + (col - 1)],
            ]
        )
        for x in proximity:
            for index in x:
                if index[2] == 1:
                    mineCount += 1
        return proximity, mineCount

    elif 0 < event[0] < (row - 1) and event[1] == (col - 1):
        proximity.append(
            [
                coordinates[coordinates.index(event) - col],
                coordinates[coordinates.index(event) - (col + 1)],
                coordinates[coordinates.index(event) - 1],
                coordinates[coordinates.index(event) + (col - 1)],
                coordinates[coordinates.index(event) + col],
            ]
        )
        for x in proximity:
            for index in x:
                if index[2] == 1:
                    mineCount += 1
        return proximity, mineCount

    elif event[0] == (row - 1) and 0 < event[1] < (col - 1):
        proximity.append(
            [
                coordinates[coordinates.index(event) - (col - 1)],
                coordinates[coordinates.index(event) - col],
                coordinates[coordinates.index(event) - (col + 1)],
                coordinates[coordinates.index(event) - 1],
                coordinates[coordinates.index(event) + 1],
            ]
        )
        for x in proximity:
            for index in x:
                if index[2] == 1:
                    mineCount += 1
        return proximity, mineCount

    elif event[0] == (row - 1) and 0 < event[1] < (col - 1):
        proximity.append(
            [
                coordinates[coordinates.index(event) - 1],
                coordinates[coordinates.index(event) + 1],
                coordinates[coordinates.index(event) + (col - 1)],
                coordinates[coordinates.index(event) + col],
                coordinates[coordinates.index(event) + (col + 1)],
            ],
        )
        for x in proximity:
            for index in x:
                if index[2] == 1:
                    mineCount += 1
        return proximity, mineCount

    elif 0 < event[0] < (row - 1) and event[1] == 0:
        proximity.append(
            [
                coordinates[coordinates.index(event) - (col - 1)],
                coordinates[coordinates.index(event) - col],
                coordinates[coordinates.index(event) + 1],
                coordinates[coordinates.index(event) + col],
                coordinates[coordinates.index(event) + (col + 1)],
            ]
        )
        for x in proximity:
            for index in x:
                if index[2] == 1:
                    mineCount += 1
        return proximity, mineCount

    elif event[0] == 0 and 0 < event[1] < (col - 1):
        proximity.append(
            [
                coordinates[coordinates.index(event) - 1],
                coordinates[coordinates.index(event) + 1],
                coordinates[coordinates.index(event) + (col - 1)],
                coordinates[coordinates.index(event) + col],
                coordinates[coordinates.index(event) + (col + 1)],
            ]
        )
        for x in proximity:
            for index in x:
                if index[2] == 1:
                    mineCount += 1
        return proximity, mineCount

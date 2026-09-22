def calc_bui(
        dmc, 
        dc
    ):

    if dmc <= (0.4 * dc):
        # Formula 27a
        bui = ((0.8 * dmc * dc) / (dmc + (0.4 * dc)))

    elif dmc > (0.4 * dc):
        # Formula 27b
        bui = dmc - ((1 - ((0.8 * dc)) / (dmc + (0.4 * dc))) * (0.92 + ((0.0114 * dmc)) ** 1.7))

    if bui < 0:
        bui = 0

    return bui
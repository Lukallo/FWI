import math

def calc_isi(
        ffmc,
        wind_1200z_kmh
    ):

    # Getting the FFMC moisture values - Reversed Formula 10
    isi_moisture_fuel = ((147.2 * (101  - ffmc)) / (59.5 + ffmc))

    # Formula no. 24
    isi_wind_function = (math.exp(0.05039 * wind_1200z_kmh))

    # Formula no. 25
    isi_ffmc_function  = (91.9 * math.exp(-0.1386 * isi_moisture_fuel) * ((1 + ((isi_moisture_fuel ** 5.31) / (4.93 * (10 ** 7))))))

    # Formula no. 26
    isi = (0.208 * isi_wind_function * isi_ffmc_function )

    return isi
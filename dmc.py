import math

DAY_LENGTH = {
        1: 6.5,
        2: 7.5,
        3: 9.0,
        4: 12.8,
        5: 13.9,
        6: 13.9,
        7: 12.4,
        8: 10.9,
        9: 9.4,
        10: 8.0,
        11: 7.0,
        12: 6.0,
    }

def calc_dmc(
        dmc_prev,
        temperature_1200z_c,
        humidity_1200z_pct, 
        rain_24h_mm,
        month
    ):

    if temperature_1200z_c < -1.1:
        temperature_1200z_c = -1.1

    dmc_rain_code = dmc_prev

    if rain_24h_mm > 1.5:
        # Formula no. 11
        dmc_effective_rain = ((0.92 * rain_24h_mm) - 1.27)
        
        # Formula no. 12
        dmc_moisture_prev = (20 + (280 / (math.exp(0.023 * dmc_prev))))

        # Formula no. 13a
        if dmc_prev <= 33:
            dmc_rain_effect_slope = (100 / (0.5 + (0.3 * dmc_prev)))

        # Formula no. 13b
        elif 33 < dmc_prev <= 65:
            dmc_rain_effect_slope = (14 - (1.3 * math.log(dmc_prev)))

        # Formula no. 13c
        elif dmc_prev > 65:
            dmc_rain_effect_slope = ((6.2 * math.log(dmc_prev)) - 17.2)

        # Formula no. 14
        dmc_moisture_rain = (dmc_moisture_prev + ((1000 * dmc_effective_rain) / (48.77 + (dmc_rain_effect_slope * dmc_effective_rain))))

        # Formula no. 15
        dmc_rain_code = (244.72 - (43.43 * math.log(dmc_moisture_rain - 20)))

        if dmc_rain_code < 0:
            dmc_rain_code = 0

    # Formula no. 16
    dmc_drying_factor = (1.894 * (temperature_1200z_c + 1.1) * (100 - humidity_1200z_pct) * DAY_LENGTH[month] * (10 ** -6))

    # Formula no. 17
    dmc = (dmc_rain_code + (100 * dmc_drying_factor))
    return dmc






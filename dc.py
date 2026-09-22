import math

DAY_LENGTH = {
        1: -1.6,   
        2: -1.6,   
        3: -1.6,  
        4:  0.9,   
        5:  3.8,   
        6:  5.8,  
        7:  6.4,   
        8:  5.0,   
        9:  2.4,   
        10: 0.4,   
        11: -1.6,  
        12: -1.6,
    }

def calc_dc( 
        dc_prev,
        temperature_1200z_c,
        rain_24h_mm,   
        month
    ):

    dc_day_length_factor = DAY_LENGTH[month]

    if temperature_1200z_c < -2.8:
        temperature_1200z_c = -2.8

    dc_rain_code = dc_prev 

    if rain_24h_mm > 2.8:

        # Formula no. 18
        dc_effective_rain = ((0.83 * rain_24h_mm) - 1.27)

        # Formula no. 19
        dc_moisture_equivalent = 800 * math.exp(-dc_prev / 400)

        # Formula no. 20
        dc_moisture_rain = (dc_moisture_equivalent + (3.937 * dc_effective_rain))

        # Formula no. 21
        dc_rain_code = 400 * math.log(800 / dc_moisture_rain)

        if dc_rain_code < 0:
            dc_rain_code = 0

    # Formula no. 22
    dc_drying_factor = ((0.36 * (temperature_1200z_c + 2.8)) + dc_day_length_factor)

    if dc_drying_factor < 0:
        dc_drying_factor = 0

    # Formula no. 23
    dc = (dc_rain_code + (0.5 * dc_drying_factor))
    return dc



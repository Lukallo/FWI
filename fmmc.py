import math

def calc_ffmc(
        ffmc_prev, 
        temperature_1200z_c,
        humidity_1200z_pct,
        wind_1200z_kmh,
        rain_24h_mm     
        ):

    # Formula no. 1
    ffmc_moisture_prev = ((147.2 * (101 - ffmc_prev)) / (59.5 + ffmc_prev))

    # Formula no. 2
    if rain_24h_mm > 0.5:

        ffmc_rain_effective = (rain_24h_mm - 0.5)
    
        # Formula no. 3a
        if ffmc_moisture_prev <= 150:
            ffmc_moisture_rain = (ffmc_moisture_prev + (42.5 * ffmc_rain_effective * (math.exp(-100/(251-ffmc_moisture_prev))) * (1 - (math.exp(-6.93/(ffmc_rain_effective))))))

        # Formula no. 3b
        elif ffmc_moisture_prev > 150:
            ffmc_moisture_rain = (ffmc_moisture_prev + (42.5 * ffmc_rain_effective * (math.exp(-100/(251 - ffmc_moisture_prev))) * (1 - (math.exp(-6.93/(ffmc_rain_effective))))) + (0.0015 * ((ffmc_moisture_prev - 150) ** 2) * (ffmc_rain_effective ** 0.5)))

    else:
        ffmc_moisture_rain = ffmc_moisture_prev

    # Formula no. 4
    ffmc_equilibrium_drying = ((0.942 * (humidity_1200z_pct ** 0.679)) + (11 * math.exp((humidity_1200z_pct - 100) / 10)) + (0.18 * (21.1 - temperature_1200z_c) * (1 - math.exp(-0.115 * humidity_1200z_pct))))

    if ffmc_moisture_rain > ffmc_equilibrium_drying:
        
        # Formula no. 6a
        ffmc_rate_base = ((0.424 * (1 - ((humidity_1200z_pct / 100) ** 1.7))) + (0.0694 * (wind_1200z_kmh ** 0.5) * (1 - ((humidity_1200z_pct / 100) ** 8))))

        # Formula no. 6b
        ffmc_drying_term = (ffmc_rate_base * 0.581 * math.exp(0.0365 * temperature_1200z_c))

        # Formula no. 8
        ffmc_moisture_final = (ffmc_equilibrium_drying + ((ffmc_moisture_rain - ffmc_equilibrium_drying) * (10 ** (-1 * ffmc_drying_term))))

    elif ffmc_moisture_rain < ffmc_equilibrium_drying:

        # Formula no. 5
        ffmc_equilibrium_wetting = ((0.618 * (humidity_1200z_pct ** 0.753)) + (10 * math.exp((humidity_1200z_pct - 100) / 10)) + (0.18 * (21.1 - temperature_1200z_c) * (1 - math.exp(-0.115 * humidity_1200z_pct))))

        if ffmc_moisture_rain < ffmc_equilibrium_wetting:

            # Formula no. 7a
            ffmc_rate_log = ((0.424 * (1 - (((100 - humidity_1200z_pct) / 100) ** 1.7))) + (0.0694 * (wind_1200z_kmh ** 0.5) * (1 - (((100 - humidity_1200z_pct) / 100) ** 8))))

            # Formula no. 7b
            ffmc_wetting_term = (ffmc_rate_log * 0.581 * math.exp(0.0365 * temperature_1200z_c))

            # Formula no. 9
            ffmc_moisture_final = (ffmc_equilibrium_wetting - ((ffmc_equilibrium_wetting - ffmc_moisture_rain) * (10 ** (-1 * ffmc_wetting_term))))
        else:
            ffmc_moisture_final = ffmc_moisture_rain
    else:
        ffmc_moisture_final = ffmc_moisture_rain

    # Formula no. 10
    ffmc = (59.5 * ((250 - ffmc_moisture_final)/(147.2 + ffmc_moisture_final)))
    return ffmc

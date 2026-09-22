# FWI library Function Documentaton

## Dependencies

math


## Parameter Order for Functions

1) Previous State
2) Weather inputs
    * Temperature, Humidity, Wind, Rain
3) Context
    * Time, Location

## Variable naming standard

quantity_time_unit

* Time can be specific time or time frame
* 24 hour time frame = "24h"
* Specific time stamp, e.g. 4PM UTC = "1600z"
    * UTC time should be used as FWI weather observations must be taken at 12:00PM LST or 13:00PM DST, in order to avoid issues, Zulu time will be used throughout.
* Unit will be based on SI Unit name e.g. "c" for Celsius
    * No solid standard found on internet
* For all previous state variables, standard will be, variable_prev, e.g. Previous FFMC state = ffmc_prev

## Variables

### Previous index values

* ffmc_prev
* dmc_prev
* dc_prev

### Weather observations

* temperature_1200z_c 
* humidity_1200z_pct
* wind_1200z_kmh
* rain_24h_mm

### Calculated values

* ffmc
* dmc
* dc
* isi
* bui
* fwi
* dsr

## FFMC Function

Returns the Fine Fuel Moisture Code (FFMC) for the current day using  the previous day's FFMC, current weather observations and the rainfall measurement over the last 24 hours.

### Function call

```python
calc_ffmc(
    ffmc_prev,
    temperature_1200z_c,
    humidity_1200z_pct,
    wind_1200z_kmh,
    rain_24h_mm
)
```

### Arguments

* ffmc_prev
    * The previous day's FFMC value
* temperature_1200z_c
    * Air temperature at 12:00 UTC
* humidity_1200z_pct
    * Relative humidity at 12:00 UTC
* wind_1200z_kmh
    * Wind speed at 12:00 UTC
* rain_24h_mm
    * Rainfall during the last 24 hours

### Return



## ISI Function

Computes the Initial Spread Index (ISI) for the current day using wind speed observation and FFMC moisture value.

### Function call

calc_ISI(noonWind, initMoist)


# FWI library reference
## Python library Dependencies

**math**  
**datetime** (If needed for month)

## Parameter Order for Functions

1. Previous state (Where applicable)
2. Current state (derived from earlier computations)
3. Weather inputs
    * Temperature, Humidity, Wind, Rain
4. Contextual information
    * Time, Location

## Variable naming standards

**quantity_time_unit**

* Time can be specific time or time frame
* 24 hour time frame = "24h"
* Specific time stamp, e.g. 4PM UTC = "1600z"
    * UTC time should be used as FWI weather observations must be taken at 12:00PM LST or 13:00PM DST, in order to avoid issues, Zulu time will be used throughout.
* Unit will be based on SI Unit name e.g. "c" for Celsius
* For all previous state variables, standard will be, variable_prev, e.g. Previous FFMC state = ffmc_prev
* Index values themselves will the acronym in lowercase. e.g. FFMC = ffmc

## Variables

### Previous index values

* <a id="ffmc_prev"></a> **ffmc_prev**<br>

    * **Description:** &nbsp; The previous day's FFMC value
    * **Data type:** &nbsp; float
    * **Unit:** &nbsp; dimensionless
    * **Valid range/Constraints:** &nbsp; 0 ≤ ffmc_prev ≤ 101

* <a id="dmc_prev"></a> **dmc_prev**<br>

    * **Description:** &nbsp; The previous day's DMC value
    * **Data type:** &nbsp; float
    * **Unit:** &nbsp; dimensionless
    * **Valid range/Constraints:** &nbsp; dmc ≥ 0

* <a id="dc_prev"></a> **dc_prev**<br>

    * **Description:** &nbsp; The previous day's DC value
    * **Data type:** &nbsp; float
    * **Unit:** &nbsp; dimensionless
    * **Valid range/Constraints:** &nbsp; dc ≥ 0

    ***

### Weather observations

* <a id="temperature_1200z_c"></a> **temperature_1200z_c**<br>  

    * **Description:** &nbsp; Air temperature at 12:00 UTC
    * **Data type:** &nbsp; float
    * **Unit:** &nbsp; degrees Celsius
    * **Valid range/Constraints:** none

* <a id="humidity_1200z_pct"></a> **humidity_1200z_pct**<br>  

    * **Description:** &nbsp; The relative humidity of the air at 12:00 UTC
    * **Data type:** &nbsp; float
    * **Unit:** &nbsp;   
    * **Valid range/Constraints:** &nbsp; 0 ≤ humidity_1200z_pct ≤ 100

* <a id="wind_1200z_kmh"></a> **wind_1200z_kmh**<br>

    * **Description:** &nbsp; The wind speed at 12:00 UTC
    * **Data type:** &nbsp; float
    * **Unit:** &nbsp; Kilometers per hour
    * **Valid range/Constraints:** &nbsp; 0 ≤ wind_1200z_kmh

* <a id="rain_24h_mm"></a> **rain_24h_mm**<br>

    * **Description:** &nbsp; The rainfall during the previous 24 hours
    * **Data type:** &nbsp; float
    * **Unit:** &nbsp; mm
    * **Valid range/Constraints:** &nbsp; 0 ≤ rain_24h_mm

    ***

### Calculated values

* <a id="ffmc"></a> **ffmc**<br>

    * **Description:** &nbsp; The current FFMC
    * **Data type:** &nbsp; float
    * **Unit:** &nbsp; dimensionless
    * **Valid range/Constraints:** &nbsp; 0 ≤ ffmc ≤ 101

* <a id="dmc"></a> **dmc**<br>

    * **Description:** &nbsp; The current DMC
    * **Data type:** &nbsp; float
    * **Unit:** &nbsp; dimensionless
    * **Valid range/Constraints:** &nbsp; 0 ≤ dmc

*  <a id="dc"></a> **dc**<br>

    * **Description:** &nbsp; The current DC
    * **Data type:** &nbsp; float
    * **Unit:** &nbsp; dimensionless
    * **Valid range/Constraints:** &nbsp; 0 ≤ dc

* <a id="isi"></a> **isi**<br>

    * **Description:** &nbsp; The current ISI
    * **Data type:** &nbsp; float
    * **Unit:** &nbsp; dimensionless
    * **Valid range/Constraints:** &nbsp; 0 ≤ isi

* <a id="bui"></a> **bui**<br>

    * **Description:** &nbsp; The current BUI
    * **Data type:** &nbsp; float
    * **Unit:** &nbsp; dimensionless
    * **Valid range/Constraints:** &nbsp; 0 ≤ bui

* <a id="fwi"></a> **fwi**<br>

    * **Description:** &nbsp; The current FWI
    * **Data type:** &nbsp; float
    * **Unit:** &nbsp; dimensionless
    * **Valid range/Constraints:** &nbsp; 0 ≤ fwi

* <a id="dsr"></a> **dsr**<br>

    * **Description:** The current DSR
    * **Data type:** float
    * **Unit:** dimensionless
    * **Valid range/Constraints:** 0 ≤ dsr
 
    ***

### Contextual values

* <a id="month"></a> **month**<br>

    * **Description:** &nbsp; The current month represented as a number
    * **Data type:** &nbsp; int
    * **Unit:** &nbsp; dimensionless
    * **Valid range/Constraints:** &nbsp; 1 ≤ month ≤ 12
    * **Example:** &nbsp; June is represented as "6"
    * **Recommended source:**
        ```python
        x = datetime.datetime.now()
        month = int(x.strftime("%m"))
        ```
        
## Order of Operations

Indices are to be calculated in the following order:

1. **FFMC**
2. **DMC**
3. **DC**
4. **ISI**
5. **BUI**
6. **FWI**
7. **DSR**

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

* [**ffmc_prev**](#ffmc_prev) 

    * The previous day's FFMC value

* [**temperature_1200z_c**](#temperature_1200z_c)

    * Air temperature at 12:00 UTC

* [**humidity_1200z_pct**](#humidity_1200z_pct)

    * Relative humidity at 12:00 UTC

* [**wind_1200z_kmh**](#wind_1200z_kmh) 

    * Wind speed at 12:00 UTC

* [**rain_24h_mm**](#rain_24h_mm) 

    * Rainfall during the last 24 hours

    ***

### Internal Variables

* **ffmc_moisture_prev $:m_o$**
* **ffmc_moisture_rain $:m_r$**
* **ffmc_moisture_final $:m$**
* **ffmc_rain_effective $:r_f$**
* **ffmc_equilibrium_drying $:E_d$**
* **ffmc_equilibrium_wetting $:E_w$**
* **ffmc_rate_base $:k_o$**
* **ffmc_rate_log $:k_l$**
* **ffmc_drying_term $:k_d$**
* **ffmc_wetting_term $:k_w$**
    ***

### Formulae

1) $m_o = 147.2 (101 - F_o) / (59.5 + F_o) $
2) $\text{if}\enspace r_o > 0.5 : \enspace {r_f} = {r_o - 0.5}$
3)  - $\text {if} \enspace {m_o <= 150}: \enspace {m_r} = {m_o + 42.5\, {r_f}\, (e^{-100/(251 - m_o)})(1 - e^{-6.93/r_f})}$
    - $\text {if} \enspace {m_o > 150}: \enspace {m_r} = {m_o + 42.5\, {r_f}\, (e^{-100/(251 - m_o)})(1 - e^{-6.93/r_f})} \enspace + \enspace {0.0015 (m_o - 150)^2 \enspace {r_f}^{0.5} } $
4) $E_d = 0.942 H^{0.679} + 11e^{(H-100)/10} + 0.18(21.1 - T)(1 - e^{-0.115H})$
5) $E_w = 0.618 H^{0.753} + 10e^{(H-100)/10} + 0.18(21.1 - T)(1 - e^{-0.115H})$
6)  - $k_o = 0.424[1-(H/100)^{1.7}] + 0.0694 W^{0.5} [1 - (H / 100)^8]$
    - $k_d = k_o \times 0.581 e^{0.0365T}$
7)  - $k_l = 0.424 [ 1- ({\frac {100 - H} {100}}) ^ {1.7} ] + 0.0694 W ^ {0.5} [1 - ({\frac {100 - H} {100}}) ^ 8]$
    - $k_w = k_l \times 0.581 e^{0.0365T}$
8) $m = E_d - (m_r - E_d) \times 10^{-k_d}$
9) $m = E_w - (E_w - m_r) \times 10^{-k_w}$
10) $F = 59.5 (250 - m) / (147.2 + m)$

### Procedure

1) Previous day's F becomes $F_o$
2) Calculate $m_o$ from $F_o$ by Formula 1
3)  - 
4) Calculate $E_d$ by Formula 4
5) 
6) If $m_o < E_d$, calculate $E_w$ by Formula 5
7) 
8) If $E_d >= m_o >= E_w$, let $m = m_o$
9) Calculate $F$ from $m$ by Formula 10 

### Returns

* [**ffmc**](#ffmc)

    * The current FFMC

    ***

### Raises

*

## DMC Function

Returns the Duff Moisture Code (DMC) for the current day using the previous day's DMC, current weather observations, the rainfall observed over the past 24h and the length of the day (derived from the current month).

### Function call

```python
calc_dmc(
    dmc_prev,
    temperature_1200z_c,
    humidity_1200z_pct,
    rain_24h_mm,
    month
)
```

### Arguments

* [**dmc_prev**](#dmc_prev)

    * The previous day's DMC value

* [**temperature_1200z_c**](#temperature_1200z_c)

    * Air temperature at 12:00 UTC

* [**humidity_1200z_pct**](#humidity_1200z_pct)

    * Relative humidity at 12:00 UTC

* [**rain_24h_mm**](#rain_24h_mm)

    * Rainfall during the last 24 hours

* [**month**](#month)

    * The current month represented as a number

    ***

### Internal Variables

* **dmc_moisture_prev $:M_o$**
* **dmc_moisture_rain $:M_r$**
* **dmc_drying_factor $:K$**
* **dmc_day_length $:L_e$**
* **dmc_rain_effect_slope $:b$**
* **dmc_rain_code $:P_r$**
* **dmc_effective_rain $:r_e$**
    ***

### Formulae

11) $\text{if}\enspace r_o > 1.5 : \enspace r_e =  0.92r_o - 1.27$

12) $M_o = 20 + 280 e ^ {-0.023P_o}$

13) - $\,\text{if}\enspace P_o <= 33 : \enspace b = 100 / (0.5 + 0.3P_o)$

    - $\,\text{if}\enspace 33 < P_o <= 65 : \enspace b = 14 - 1.3\ln{P_o}$

    - $\,\text{if}\enspace P_o > 65 : \enspace b = 6.2\ln{P_o} - 17.2$

14) $M_r = M_o + 1000{r_e}/{(48.77 + {b}{r_e})}$

15) $P_r = 244.72 - 43.43\ln{(M_r - 20)}$

16) $K = 1.894{(T + 1.1)(100 - H)(L_e \times 10^{-6})}$

17) $P = P_o \enspace\text{(or\,}P_r) + 100K$
    ***

### Procedure

1) Previous day's $P$ becomes $P_o$
2) 
3) Take $L_e$ from Table 1
4) Calculate $K$ by Formula 16
5) Calculate $P$ from $P_o$ or $P_r$ by Formula 17

### Returns

* [**dmc**](#dmc)

    * The current DMC

    ***

### Raises

***


## DC Function

Returns the Drought Code (DC) for the current day using the previous day's DC, current air temperature, rainfall recorded over the past 24 hours and the length of day (derived from the current month)

### Function call

```python
calc_dc(
    dc_prev,
    temperature_1200z_c,
    rain_24h_mm,
    month
)
```

### Arguments

* [**dc_prev**](#dc_prev)

    * The previous day's DC value

* [**temperature_1200z_c**](#temperature_1200z_c)

    * Air temperature at 12:00 UTC

* [**rain_24h_mm**](rain_24h_mm)

    * Rainfall during the last 24 hours

* [**month**](#month)

    * The current month represented as a number

    ***

### Internal Variables

* **dc_moisture_equivalent $:Q_o$**
* **dc_moisture_rain $:Q_r$**
* **dc_effective_rain $:r_d$**
* **dc_drying_factor $:V$**
* **dc_day_length_factor $:L_f$**
* **dc_rain_code $:D_r$**

    ***

### Formulae

18) $\text {if} \enspace {r > 2.8:} \enspace r_d = 0.83 r_o - 1.27$
19) $Q_o = 800 e^{-D_o / 400}$
20) $Q_r = Q_o + 3.937 r_d$
21) $D_r = 400 \ln{(800 / Q_r)}$
22) $V = 0.36 (T + 2.8) + L_f $
23) $D = D_r + 0.5V $

    ***

### Procedure

1) The previous day's $D$ becomes $D_o$
2) 
3) Take $L_f$ from Table 2

### Returns

* [**dc**](#dc)

    * The current Drought Code

    ***

### Raises
## ISI Function

Returns the Initial Spread Index (ISI) for the current day using wind speed observation and FFMC moisture value.

### Function call

```python
calc_isi(
    ffmc,
    wind_1200z_kmh
)
```

### Arguments

* [**ffmc**](#ffmc)

    * The current FFMC value

* [**wind_1200z_kmh**](#wind_1200z_kmh)
    * Wind speed at 12:00 UTC

    ***

### Internal Variables

* **isi_moisture_fuel $:m$**
* **isi_wind_function $:f(W)$**
* **isi_ffm_function $:f(F)$**

    ***

### Formulae

24) $f(W) = e ^ {0.05039 W}$
25) $f(F) = 91.9 e ^ {-0.1386 m} [{1 + m ^ {5.31}} / {(4.93 \times 10 ^ 7)}]$
26) $R = 0.208 f(W) f(F)$

    ***

### Procedure

1) Calculate $f(W)$ and $f(F)$ by Formulae 24 and 25
2) Calcuate $R$ by Formula 26

### Returns

* [**isi**](#isi)

    * The current Initial Spread Index

    ***

### Raises
## BUI Function

Returns the Buildup Index given the current DMC and DC

### Function call

```python
calc_bui(
    dmc,
    dc
)
```

### Arguments

* [**dmc**](#dmc)

    * The current DMC value

* [**dc**](#dc)

    * The current DC value

    ***

### Internal Variables

* **d

### Formulae
27) - $\text{if} \enspace {P <= 0.4D:} \enspace U = {0.8 P D} / {(P + 0.4D)}$
    - $\text{if} \enspace {P > 0.4D:} \enspace U = P - [{1 - 0.8D} / (P + 0.4D)][0.92 + (0.0114P)^{1.7}]$

### Procedure

1) Calculate $U$ by Formula 27a or 27b

### Returns

* [**bui**](#bui)

    * The current BUI

    ***

### Raises

## FWI Function

Returns the Fire Weather Index

### Function call

```python
calc_fwi(
    isi,
    bui
)
```
### Arguments

* [**isi**](#isi)

    * The current Initial Spread Index

* [**bui**](#bui)

    * The current Build Up Index

    ***

### Internal Variables

* **fwi_duff_function $:f(D)$**
* **fwi_intermediate $:B$**

### Formulae

28) 
29) $B = 0.1 R f(D)$
30) 

### Procedure

1) Calculate $f(D)$ by Formula 28a or 28b
2) Calculate $B$ by Formula 29
3) Calculate $S$ by Formula 30a or 30b

### Returns

* [**fwi**](#fwi)

    * The current FWI

    ***

### Raises

## DSR Function

<p> Returns the Daily Spread Rate (DSR) for the current day using the current FWI </p>

### Function call

```python
calc_dsr(
    fwi
)
```

### Arguments

* [**fwi**](#fwi)

    * The current FWI

    ***

### Formula

31) $DSR = 0.0272(FWI)^{1.77}$

### Returns

* [**dsr**](#dsr)

    * The current DSR

    ***

### Raises

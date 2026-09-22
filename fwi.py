import math

def calc_fwi(
        isi,
        bui
    ):
    
    if bui <= 80:
        # Formula no. 28a
        fwi_duff_function = ((0.626 * (bui ** 0.809)) + 2)

    elif bui > 80:
        # Formula no. 28b
        fwi_duff_function = (1000 / (25 + (108.64 * math.exp(-0.023 * bui))))

    # Formula no. 29
    fwi_intermediate = (0.1 * isi * fwi_duff_function)

    if fwi_intermediate > 1:
        # Formula no. 30a
        fwi = math.exp(2.72 * ((0.434 * math.log(fwi_intermediate)) ** 0.647))
        
    elif fwi_intermediate <= 1:
        # Formula no. 30b
        fwi = fwi_intermediate

    return fwi
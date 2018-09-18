

# They sort of have fixed positions,
# so troll through the dictionary picking up the band groups
def imd_bands(imd_dict):
    band_dict = {}
    ordinal = 1
    for key, value in imd_dict.items():
        if key.startswith('BAND'):
            band_dict[key[5:]] = ordinal
            ordinal += 1
    return band_dict

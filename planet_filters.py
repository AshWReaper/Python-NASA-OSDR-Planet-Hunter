# ========== Filter Settings ==========
FILTERS = {
    "radius_range": (0.8, 1.8),          # Earth radii
    "orbital_period_range": (150, 500),  # days
    "temp_range": (180, 350),            # equilibrium temp (K)
    "stellar_temp_range": (4700, 6500),  # K (Sun ~5778K)
    "stellar_radius_range": (0.6, 1.5)   # Solar radii
}

# ========== Helper ==========
def is_earth_like(planet, require_all=True):
    match_count = 0
    total_criteria = 5
    try:
        if FILTERS["radius_range"][0] <= planet["pl_rade"] <= FILTERS["radius_range"][1]:
            match_count += 1
        if FILTERS["orbital_period_range"][0] <= planet["pl_orbper"] <= FILTERS["orbital_period_range"][1]:
            match_count += 1
        if FILTERS["temp_range"][0] <= planet["pl_eqt"] <= FILTERS["temp_range"][1]:
            match_count += 1
        if FILTERS["stellar_temp_range"][0] <= planet["st_teff"] <= FILTERS["stellar_temp_range"][1]:
            match_count += 1
        if FILTERS["stellar_radius_range"][0] <= planet["st_rad"] <= FILTERS["stellar_radius_range"][1]:
            match_count += 1
        if require_all:
            return match_count == total_criteria
        else:
            return match_count >= 3  # return if 3 or more criteria match
    except (TypeError, KeyError):
        return False

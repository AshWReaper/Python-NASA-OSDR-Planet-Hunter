import os
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from planet_filters import is_earth_like

# ========== Config ==========
NASA_API_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
QUERY = """
SELECT pl_name, pl_orbper, pl_rade, pl_eqt, st_teff, st_rad, st_mass
FROM ps
WHERE default_flag = 1
"""

# Toggle full match requirement via env var or default to False
REQUIRE_ALL_CRITERIA = os.getenv("REQUIRE_ALL_CRITERIA", "false").lower() == "true"

# ========== Query Function ==========
def query_nasa_exoplanets():
    print("Fetching data from NASA Exoplanet Archive...")

    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))

    response = session.post(NASA_API_URL, data={
        "query": QUERY,
        "format": "json"
    }, timeout=10)
    response.raise_for_status()
    return response.json()

# ========== Main ==========
def main():
    print(f"[Filter Mode] REQUIRE_ALL_CRITERIA = {REQUIRE_ALL_CRITERIA}")
    planets = query_nasa_exoplanets()
    matches = [p for p in planets if is_earth_like(p, REQUIRE_ALL_CRITERIA)]

    print(f"\nFound {len(matches)} potential Earth-like exoplanets:\n")
    for planet in matches:
        print(f"- {planet['pl_name']} (Radius: {planet.get('pl_rade', '?')} R\u2295, Temp: {planet.get('pl_eqt', '?')} K, Star Temp: {planet.get('st_teff', '?')} K)")

if __name__ == "__main__":
    main()

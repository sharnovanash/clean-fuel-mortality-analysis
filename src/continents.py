"""Country -> continent lookup, using WHO country names."""

CONTINENT_MAP = {
    # Asia
    "Afghanistan": "Asia", "Armenia": "Asia", "Azerbaijan": "Asia", "Bahrain": "Asia",
    "Bangladesh": "Asia", "Bhutan": "Asia", "Brunei Darussalam": "Asia", "Cambodia": "Asia",
    "China": "Asia", "Democratic People's Republic of Korea": "Asia", "India": "Asia",
    "Indonesia": "Asia", "Iran (Islamic Republic of)": "Asia", "Iraq": "Asia",
    "Israel": "Asia", "Japan": "Asia", "Jordan": "Asia", "Kazakhstan": "Asia",
    "Kuwait": "Asia", "Kyrgyzstan": "Asia", "Lao People's Democratic Republic": "Asia",
    "Lebanon": "Asia", "Malaysia": "Asia", "Maldives": "Asia", "Mongolia": "Asia",
    "Myanmar": "Asia", "Nepal": "Asia", "Oman": "Asia", "Pakistan": "Asia",
    "Philippines": "Asia", "Qatar": "Asia", "Republic of Korea": "Asia",
    "Saudi Arabia": "Asia", "Singapore": "Asia", "Sri Lanka": "Asia",
    "Syrian Arab Republic": "Asia", "Tajikistan": "Asia", "Thailand": "Asia",
    "Timor-Leste": "Asia", "Turkey": "Asia", "Turkmenistan": "Asia",
    "United Arab Emirates": "Asia", "Uzbekistan": "Asia", "Viet Nam": "Asia", "Yemen": "Asia",

    # Europe
    "Albania": "Europe", "Andorra": "Europe", "Austria": "Europe", "Belarus": "Europe",
    "Belgium": "Europe", "Bosnia and Herzegovina": "Europe", "Bulgaria": "Europe",
    "Croatia": "Europe", "Cyprus": "Europe", "Czechia": "Europe", "Denmark": "Europe",
    "Estonia": "Europe", "Finland": "Europe", "France": "Europe", "Georgia": "Europe",
    "Germany": "Europe", "Greece": "Europe", "Hungary": "Europe", "Iceland": "Europe",
    "Ireland": "Europe", "Italy": "Europe", "Latvia": "Europe", "Liechtenstein": "Europe",
    "Lithuania": "Europe", "Luxembourg": "Europe", "Malta": "Europe", "Monaco": "Europe",
    "Montenegro": "Europe", "Netherlands": "Europe", "North Macedonia": "Europe",
    "Norway": "Europe", "Poland": "Europe", "Portugal": "Europe",
    "Republic of Moldova": "Europe", "Romania": "Europe", "Russian Federation": "Europe",
    "San Marino": "Europe", "Serbia": "Europe", "Slovakia": "Europe", "Slovenia": "Europe",
    "Spain": "Europe", "Sweden": "Europe", "Switzerland": "Europe",
    "The former Yugoslav Republic of Macedonia": "Europe", "Ukraine": "Europe",
    "United Kingdom": "Europe",
    "United Kingdom of Great Britain and Northern Ireland": "Europe",

    # Africa
    "Algeria": "Africa", "Angola": "Africa", "Benin": "Africa", "Botswana": "Africa",
    "Burkina Faso": "Africa", "Burundi": "Africa", "Cabo Verde": "Africa",
    "Cameroon": "Africa", "Central African Republic": "Africa", "Chad": "Africa",
    "Comoros": "Africa", "Congo": "Africa", "Côte d’Ivoire": "Africa",
    "Democratic Republic of the Congo": "Africa", "Djibouti": "Africa", "Egypt": "Africa",
    "Equatorial Guinea": "Africa", "Eritrea": "Africa", "Eswatini": "Africa",
    "Ethiopia": "Africa", "Gabon": "Africa", "Gambia": "Africa", "Ghana": "Africa",
    "Guinea": "Africa", "Guinea-Bissau": "Africa", "Kenya": "Africa", "Lesotho": "Africa",
    "Liberia": "Africa", "Libya": "Africa", "Madagascar": "Africa", "Malawi": "Africa",
    "Mali": "Africa", "Mauritania": "Africa", "Mauritius": "Africa", "Morocco": "Africa",
    "Mozambique": "Africa", "Namibia": "Africa", "Niger": "Africa", "Nigeria": "Africa",
    "Rwanda": "Africa", "Sao Tome and Principe": "Africa", "Senegal": "Africa",
    "Seychelles": "Africa", "Sierra Leone": "Africa", "Somalia": "Africa",
    "South Africa": "Africa", "South Sudan": "Africa", "Sudan": "Africa",
    "Tanzania": "Africa", "Togo": "Africa", "Tunisia": "Africa", "Uganda": "Africa",
    "United Republic of Tanzania": "Africa", "Zambia": "Africa", "Zimbabwe": "Africa",

    # North America (incl. Central America & Caribbean)
    "Antigua and Barbuda": "North America", "Bahamas": "North America",
    "Barbados": "North America", "Belize": "North America", "Canada": "North America",
    "Costa Rica": "North America", "Cuba": "North America", "Dominica": "North America",
    "Dominican Republic": "North America", "El Salvador": "North America",
    "Grenada": "North America", "Guatemala": "North America", "Haiti": "North America",
    "Honduras": "North America", "Jamaica": "North America", "Mexico": "North America",
    "Nicaragua": "North America", "Panama": "North America",
    "Saint Kitts and Nevis": "North America", "Saint Lucia": "North America",
    "Saint Vincent and the Grenadines": "North America",
    "Trinidad and Tobago": "North America", "United States of America": "North America",

    # South America
    "Argentina": "South America", "Bolivia (Plurinational State of)": "South America",
    "Brazil": "South America", "Chile": "South America", "Colombia": "South America",
    "Ecuador": "South America", "Guyana": "South America", "Paraguay": "South America",
    "Peru": "South America", "Suriname": "South America", "Uruguay": "South America",
    "Venezuela": "South America", "Venezuela (Bolivarian Republic of)": "South America",

    # Oceania
    "Australia": "Oceania", "Fiji": "Oceania", "Kiribati": "Oceania",
    "Marshall Islands": "Oceania", "Micronesia (Federated States of)": "Oceania",
    "Nauru": "Oceania", "New Zealand": "Oceania", "Palau": "Oceania",
    "Papua New Guinea": "Oceania", "Samoa": "Oceania", "Solomon Islands": "Oceania",
    "Tonga": "Oceania", "Tuvalu": "Oceania", "Vanuatu": "Oceania",
}

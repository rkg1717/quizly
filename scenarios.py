# scenarios.py

WEATHER_SCENARIOS = {
    1: {
        "title": "Late Afternoon Spring Transition",
        "location": "Tri-State Forecast Area",
        "time_of_day": "3:30 PM, Mid-May",
        "modes": {
            "novice": {
                "sky_look": "The horizon is turning a bruised, greenish-black. Low, ragged clouds are rushing northward just above the tree line.",
                "instruments": "Your patio weather station shows the temperature at 86°F with a suffocating humidity. The barometer needle has been dropping steadily for the last two hours.",
                "environment": "The air feels heavy and completely still, but the clouds high above are racing in a completely different direction than the low-level clouds.",
                "reports": "Local law enforcement reports a wall cloud dropping down just two counties to your west."
            },
            "experienced": {
                "thermodynamics": "Model soundings show a raw CAPE of 3,400 J/kg with a Lifted Index (LI) of -7. A weakening capping inversion (CIN of -20 J/kg) is rapidly eroding due to daytime heating.",
                "kinematics": "0-6 km Bulk Shear is clocked at 55 knots, perpendicular to the surface boundary. 0-1 km Storm-Relative Helicity (SRH) is spiking at 320 m²/s² along a stalled warm front.",
                "dynamics": "A vigorous 500mb shortwave trough is moving into the region, placing your zone in the left-front quadrant of a 90-knot jet streak.",
                "surface_obs": "Surface Temp: 86°F, Dew Point: 74°F. Altimeter: 29.62 inHg and falling (dropped 4mb in 2 hours). A sharp dryline is actively colliding with the moist marine air mass."
            }
        },
        "scoring_targets": {
            "correct_alert": "tornado_warning", 
            "min_lead_time": 15,                
            "max_lead_time": 40,                
            "ideal_lead_time": 25,              
            "hail_magnitude": "golf_ball",
            "wind_magnitude": "70mph",
            "tornado_magnitude": "ef2_ef3"
        },
        "verification_text": "A discrete, classic supercell thunderstorm tracked directly across the forecast area, producing a rain-wrapped EF2 tornado and golf-ball-sized hail that caused significant property damage."
    },
    2: {
        "title": "Midsummer Heat Wave Collapse",
        "location": "Midwest Metro Corridor",
        "time_of_day": "5:15 PM, Late July",
        "modes": {
            "novice": {
                "sky_look": "A solid, imposing wall of dark grey clouds stretching from horizon to horizon is advancing rapidly from the northwest, preceded by a massive, low-hanging shelf cloud.",
                "instruments": "The temperature has peaked at a blistering 96°F. The wind gauge was dead calm all afternoon but has suddenly spiked to a sustained northwest wind of 35 mph ahead of the rain.",
                "environment": "A sudden, violent blast of cool air drops the temperature 15 degrees in under three minutes, kicking up blinding dust across the area.",
                "reports": "Airport weather radar shows an intense bow echo moving southeast at 60 mph, with widespread reports of tree damage upstream."
            },
            "experienced": {
                "thermodynamics": "Extreme thermodynamic instability is present with CAPE values pooling at 4,500 J/kg and an LI of -9. The atmosphere is completely uncapped (CIN is 0 J/kg) after days of intense solar heating.",
                "kinematics": "0-6 km Bulk Shear is strong at 45 knots and strictly unidirectional. 0-1 km SRH is minimal (less than 50 m²/s²), showing nearly linear wind vectors throughout the lower boundary layer.",
                "dynamics": "An upper-level disturbance is riding along a sagging, progressive cold front, triggering a massive, consolidated linear convective system (MCS).",
                "surface_obs": "Surface Temp: 96°F, Dew Point: 76°F. Altimeter: 29.80 inHg. A distinct, severe micro-mesohigh is developing directly behind the leading gust front."
            }
        },
        "scoring_targets": {
            "correct_alert": "severe_warning",
            "ideal_lead_time": 35,
            "hail_magnitude": "quarter",
            "wind_magnitude": "80mph"
        },
        "verification_text": "A severe, progressive Derecho slammed into the metro corridor. Linear straight-line winds topped out at 83 mph, flattening construction sites, snapping utility poles, and causing widespread power grid failures, accompanied by brief pockets of quarter-sized hail."
    },
    3: {
        "title": "Uncapped Tropical Gulf Air Mass",
        "location": "Southeast Coastal Plain",
        "time_of_day": "1:00 PM, Early August",
        "modes": {
            "novice": {
                "sky_look": "The sky is a hazy blue, dotted with typical puffy white summer clouds that are slowly growing taller into localized, scattered thunderheads.",
                "instruments": "Temperature is 91°F with high humidity. The barometer is steady and showing normal summer patterns with no major changes.",
                "environment": "Winds are practically non-existent. Individual storms are visibly going up, dumping heavy downpours on one neighborhood while leaving the next street completely dry.",
                "reports": "The local weather office reports scattered, pulse-like summer thunderstorms that are moving incredibly slowly, remaining nearly stationary over local watersheds."
            },
            "experienced": {
                "thermodynamics": "Moderate, widespread pulse instability is present with a CAPE of 1,800 J/kg. There is zero convective inhibition (CIN), allowing for easy cloud growth with daytime heating.",
                "kinematics": "Atmospheric steering winds are incredibly weak. 0-6 km Bulk Shear is negligible at 10 knots, and low-level helicity (SRH) is near zero, indicating a complete lack of storm organization or rotation vectors.",
                "dynamics": "No major frontal boundaries, troughs, or jet streaks are present. Convection is driven strictly by localized solar heating and sea-breeze convergence loops.",
                "surface_obs": "Surface Temp: 91°F, Dew Point: 75°F. Altimeter: 30.02 inHg and holding flat. Precipitable Water (PWAT) values are exceptionally high at 2.2 inches."
            }
        },
        "scoring_targets": {
            "correct_alert": "none", 
            "ideal_lead_time": 0,
            "hail_magnitude": "none",
            "wind_magnitude": "none"
        },
        "verification_text": "Typical pulse summer thunderstorms developed across the region. Because steering currents were dead, individual cells rained themselves out within 45 minutes over the same spots, causing localized street flooding but no severe hail or organized wind damage."
    }
}
from typing import Dict, Any


def get_default_liquids() -> Dict[str, Dict[str, Any]]:
   
     return {
        "water": {"name": "Water (H2O)", "freezing_point": 0.0, "boiling_point": 100.0},
        "ethanol": {"name": "Ethanol (C₂H₅OH)", "freezing_point": -114.1, "boiling_point": 78.4},
        "milk": {"name": "Milk", "freezing_point": -0.5, "boiling_point": 100.2}
        }



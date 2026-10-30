from typing import Optional


def calculate_pressure_effect(base_boiling_point: float, pressure: float) -> Optional[float]:
   adjusted_boiling_point = base_boiling_point + (pressure - 1.0) * 10.0    
   return adjusted_boiling_point



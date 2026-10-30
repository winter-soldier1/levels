from typing import Optional

def decide_state(temperature: float, freezing_point: float, actual_boiling_point: float) -> Optional[str]:
    if temperature <= freezing_point:
        result_state = "SOLID"
    elif temperature >= actual_boiling_point:
      result_state = "GAS"
    else:
        result_state = "LIQUID"
  
    return result_state



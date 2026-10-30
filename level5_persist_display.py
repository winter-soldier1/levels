from typing import Dict, Any
import json
import os


def save_analysis_result(results: Dict[str, Any], filename: str = "data/analysis_results.json") -> bool:
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                all_results = json.load(f)
        else:
            all_results = []
        all_results.append(results)
        with open(filename, 'w') as f:
            json.dump(all_results, f, indent=2)
        return True
    except Exception:
        return False


def format_results_text(results: Dict[str, Any]) -> str:
    line1 = f"Liquid: {results['liquid_name']}"
    line2 = f"Temperature: {results['temperature']}°C"
    line3 = f"Pressure: {results['pressure']} atm"
    line4 = f"STATE: {results['state'].upper()}"
    line5 = f"Freezing point: {results['freezing_point']}°C"
    line6 = f"Boiling point (normal): {results['boiling_point_normal']}°C"
    line7 = f"Boiling point (actual): {results['boiling_point_actual']}°C"
    return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5 + '\n' + line6 + '\n' + line7

import json
import random

def generate_prediction(match_data):
    home_team = match_data.get('homeTeam', {}).get('name', 'Unknown')
    away_team = match_data.get('awayTeam', {}).get('name', 'Unknown')
    match = f"{home_team} vs {away_team}"
    
    # Mock prediction logic
    home_win_prob = random.uniform(0.3, 0.7)
    draw_prob = random.uniform(0.1, 0.3)
    away_win_prob = 1 - home_win_prob - draw_prob
    
    outcomes = {
        'home_win': round(home_win_prob * 100, 1),
        'draw': round(draw_prob * 100, 1),
        'away_win': round(away_win_prob * 100, 1)
    }
    
    confidence = random.randint(3, 5)
    key_factors = [
        "Recent home team performance",
        "Away team fatigue from travel",
        "Historical head-to-head results"
    ]
    narrative = f"Based on recent form, {home_team} has a slight edge."
    
    return {
        'match': match,
        'outcomes': outcomes,
        'confidence': confidence,
        'key_factors': key_factors,
        'narrative': narrative
    }

if __name__ == '__main__':
    input_data = json.loads(input())
    predictions = [generate_prediction(match) for match in input_data]
    print(json.dumps(predictions))
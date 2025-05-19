import json
import random
import sys

def generate_prediction(match_data):
    # Extract match details from API response
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
    narrative = f"Based on recent performance and historical data, {home_team} has a slight edge due to strong home form."
    
    return {
        'match': match,
        'outcomes': outcomes,
        'confidence': confidence,
        'key_factors': key_factors,
        'narrative': narrative
    }

if __name__ == '__main__':
    # Read input from stdin (for n8n or file redirection)
    input_data = sys.stdin.read()
    try:
        # Parse the JSON input
        data = json.loads(input_data)
        # Extract matches (handles API response structure)
        matches = data.get('matches', [])
        predictions = [generate_prediction(match) for match in matches]
        print(json.dumps(predictions))
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)
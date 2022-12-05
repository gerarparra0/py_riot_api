available_regions = {
    'NA': ['na1.api.riotgames.com', 'americas.api.riotgames.com'],
    'LA': ['la1.api.riotgames.com', 'americas.api.riotgames.com'],
    'BR': ['br1.api.riotgames.com', 'americas.api.riotgames.com'],
    
    'EUW': ['euw1.api.riotgames.com', 'europe.api.riotgames.com'],
    'EUN': ['eun1.api.riotgames.com', 'europe.api.riotgames.com'],
    'RU': ['ru.api.riotgames.com', 'europe.api.riotgames.com'],
    'TR': ['tr1.api.riotgames.com', 'europe.api.riotgames.com'],
    
    'KR': ['kr.api.riotgames.com', 'asia.api.riotgames.com'],
    'JP': ['jp1.api.riotgames.com', 'asia.api.riotgames.com'],
    
    'OC': ['oc1.api.riotgames.com', 'sea.api.riotgames.com'],
}

def gen_error(status: int, description: str, message: str):
    return {status: {description: message}}
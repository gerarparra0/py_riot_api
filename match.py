import constants, key
import requests

def list_by_puuid(puuid: str, region: str, start=0, count=20, queue=None):
    if region not in constants.available_regions:
        return constants.gen_error(406, 'Error', 'Region is not available')
    
    res = None
    
    if queue is None:
        res = requests.get(
            f'https://{constants.available_regions[region][1]}/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}',
            headers={'X-Riot-Token': key.API_KEY})
    else:
        res = requests.get(
            f'https://{constants.available_regions[region][1]}/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}&queue={queue}',
            headers={'X-Riot-Token': key.API_KEY})
    
    if res.status_code != 200:
        return constants.gen_error(res.status_code, 'Error', 'Riot API returned error.')
    
    return res.json()

def by_match_id(match_id: str, region: str):
    if region not in constants.available_regions:
        return constants.gen_error(406, 'Error', 'Region is not available')
    
    res = requests.get(
        f'https://{constants.available_regions[region][1]}/lol/match/v5/matches/{match_id}',
        headers={'X-Riot-Token': key.API_KEY})
    
    if res.status_code != 200:
        return constants.gen_error(res.status_code, 'Error', 'Riot API returned error.')
    
    return res.json()
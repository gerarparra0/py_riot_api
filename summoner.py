import constants, key
import requests

def by_name(name: str, region: str):
    if region not in constants.available_regions:
        return constants.gen_error(406, 'Error', 'Region is not available')
    
    res = requests.get(
        f'https://{constants.available_regions[region][0]}/lol/summoner/v4/summoners/by-name/{name}', 
        headers={'X-Riot-Token': key.API_KEY})
    
    if res.status_code != 200:
        return constants.gen_error(res.status_code, 'Error', 'Riot API returned error')
    
    return res.json()
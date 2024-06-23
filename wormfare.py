import requests
from colorama import Fore, Style
from datetime import datetime
import urllib.parse
import time
import json
import random

LoginUrl = 'https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/auth/login'
ProfileUrl = 'https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/user/profile'
QuestUrl = 'https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/quest'
SaveClicks = 'https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/game/save-clicks'
ShopUrl = 'https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/game/shop'
ActiveBooster = 'https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/game/activate-daily-boost'
BuyBoost = 'https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/game/buy-boost'
CheckCompletion = 'https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/quest/check-completion'
claimReward = 'https://elcevb3oz4.execute-api.eu-central-1.amazonaws.com/quest/claim-reward'
minSlap = 250
maxSlap = 5000

ListTask = [
    "_LegendaryLeagueQuest",
"_MythicLeagueQuest",
"_JoinSquadQuest",
"_JoinDiscordQuest",
"_JoinInstagramQuest",
"_JoinTikTokQuest",
"_JoinYoutubeQuest",
"_EpicLeagueQuest",
"_JoinTwitterQuest",
"_WatchWormfareVideoQuest"
]

def RandomSlap(minSlap, maxSlap):
    return random.randint(minSlap, maxSlap)

LoginHeaders = {
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "en-US,en;q=0.9",
  "Content-Length": "305",
  "Content-Type": "application/json",
  "Origin": "https://clicker.wormfare.com",
  "Priority": "u=1, i",
  "Referer": "https://clicker.wormfare.com/",
  "Sec-Ch-Ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "cross-site",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

def get_headers (token):
    return{
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": f'Bearer {token}',
        "Origin": "https://clicker.wormfare.com",
        "Priority": "u=1, i",
        "Referer": "https://clicker.wormfare.com/",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "X-Api-Key": "9m60AhO1I9JmrYIsWxMnThXbF3nDW4GHFA1rde5PKzJmRA9Dv6LZ2YXSM6vvwigC"
        }

def read_init_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def complete_tasks_ceo(headers):
        for task_sub_id in [0, 1]:
            payload = {"questId": '_Followthe CEO', "taskId": task_sub_id}
            check_completion = requests.post(CheckCompletion, headers=headers, json=payload)
            if check_completion.status_code == 200:
                print(f"{Fore.GREEN}[ Task ] : Task _Followthe CEO checked for completion.")
                claim_reward = requests.post(claimReward, headers=headers, json=payload)
                if claim_reward.status_code == 200:
                    print(f"{Fore.GREEN}[ Task ] : Reward for _Followthe CEO claimed successfully.")
                else:
                    print(f"{Fore.RED}[ Task ] : Failed to claim reward for _Followthe CEO.")
            else:
                print(f"{Fore.RED}[ Task ] : Failed to check completion for _Followthe CEO.")


def complete_tasks(headers):
    for task_id in ListTask:
        payload = {"questId": task_id}
        check_completion = requests.post(CheckCompletion, headers=headers, json=payload)
        if check_completion.status_code == 200:
            print(f"{Fore.GREEN}[ Task ] : Task {task_id} checked for completion.")
            claim_reward = requests.post(claimReward, headers=headers, json=payload)
            if claim_reward.status_code == 200:
                print(f"{Fore.GREEN}[ Task ] : Reward for {task_id} claimed successfully.")
            else:
                print(f"{Fore.RED}[ Task ] : Failed to claim reward for {task_id}.")
        else:
            print(f"{Fore.RED}[ Task ] : Failed to check completion for {task_id}.")

def get_daily_boost(shop_url,headers):
    response = requests.get(shop_url, headers=headers)
    response.raise_for_status()
    return response.json().get('dailyBoosts')



def main():
    auto_tasks = input("Auto claim Task? Y/N: ").strip().upper()
    recharge_slaps = input("Using Recharge Slaps? Y/N: ").strip().upper()
    auto_booster = input("Using Floppy Fish? Y/N: ").strip().upper()
    # auto_upgrade = input("Upgrade Boosters? Y/N: ").strip().upper()
    query_data_list = read_init_data('initdata.txt')
    akun = 1
    total_accounts = len(query_data_list)
    print(f"\n\n{Fore.CYAN+Style.BRIGHT}==============Menemukan {total_accounts} akun=================\n")

    while True:
        for query_data in query_data_list:
            print(f"\n\n{Fore.CYAN+Style.BRIGHT}==============Akun {akun}=================\n")
            akun += 1
            server_time_difference = int(24000)
            current_timestamp_seconds = time.time()
            adjusted_timestamp = int(current_timestamp_seconds * 1000) - server_time_difference
            data = json.dumps({"initData": query_data})
            energyLeft = 0

            response = requests.post(LoginUrl, headers=LoginHeaders, data=data)
            
            if response.status_code == 200:
                response_data = response.json()
                token = response_data.get('accessToken')
                if token:
                    profile_headers = get_headers(token)
                    profile_response = requests.get(ProfileUrl, headers=profile_headers)
                    checkShop = get_daily_boost(ShopUrl, profile_headers)
                    full_energy = next((boost['availableCount'] for boost in checkShop if boost['type'] == 'full_energy'), None)
                    turbo = next((boost['availableCount'] for boost in checkShop if boost['type'] == 'turbo'), None)

                    if profile_response.status_code == 200:
                        profile_data = profile_response.json()
                        resetPayload = {
                            "amount" : 1,
                            "isTurbo" : False,
                            "startTimeStamp" : adjusted_timestamp
                        }
                        resetEnergy = requests.post(SaveClicks, headers=profile_headers, json=resetPayload)
                        profile_response = requests.get(ProfileUrl, headers=profile_headers)
                        energyLeft = resetEnergy.json().get('energyLeft')
                        print(f"{Fore.BLUE}[ Profile ] : Nama Akun: {profile_data.get('fullName')}")
                        print(f"{Fore.BLUE}[ Profile ] : Score: {profile_data.get('score')}")
                        print(f"{Fore.BLUE}[ Profile ] : Sisa Energy: ", energyLeft)
                        print(f"{Fore.BLUE}[ Profile ] : Recharge Full Energy: ", full_energy)
                        print(f"{Fore.BLUE}[ Profile ] : Turbo: ", turbo)
                    else:
                        print(f"{Fore.RED}[ Profile ] : Profile request failed: {profile_response.status_code}, {profile_response.text}")
                    
                    energyLeft = profile_data.get('energyLeft')
                    slapAmount = RandomSlap(minSlap, maxSlap)

                    if auto_tasks == 'Y':
                        complete_tasks(profile_headers)
                        complete_tasks_ceo(profile_headers)

                    if auto_booster == 'Y' and turbo > 0:
                        turbo_payload = {
                            "type": "turbo"
                        }
                        responseBooster = requests.post(ActiveBooster, headers=profile_headers, json=turbo_payload)
                        if responseBooster.status_code != 200:
                            print(f"{Fore.RED}[ Booster ] : Gagal mengaktifkan turbo!")
                        else:
                            print(f"{Fore.GREEN}[ Booster ] : Sukses mengaktifkan turbo!")

                    while energyLeft > 0:
                        slapPayload = {
                            "amount" : slapAmount,
                            "isTurbo" : False,
                            "startTimeStamp" : adjusted_timestamp
                        }
                        slapPayloadTurbo = {
                            "amount" : slapAmount,
                            "isTurbo" : True,
                            "startTimeStamp" : adjusted_timestamp
                        }
                        turboTrue = requests.get(ProfileUrl, headers=profile_headers)
                        turboTrue = turboTrue.json().get('isTurboAvailable')

                        if turboTrue:
                            slapResponse = requests.post(SaveClicks, headers=profile_headers, json=slapPayloadTurbo)
                        else:
                            slapResponse = requests.post(SaveClicks, headers=profile_headers, json=slapPayload)
                        if slapResponse.status_code == 200:
                            print(f"{Fore.GREEN}[ Slap ] : Sukses Slap")
                        else:
                            print(f"{Fore.RED}[ Slap ] : Gagal Slap")
                        energyLeft = requests.get(ProfileUrl, headers=profile_headers).json().get('energyLeft')
                        if energyLeft < 10 and recharge_slaps == 'Y' and full_energy > 0:
                            rechargePayload = {
                                    "type" : "full_energy"
                                }
                            responseRechargeSlaps = requests.post(ActiveBooster, headers=profile_headers, json=rechargePayload)
                            if responseRechargeSlaps.status_code == 200:
                                print(f"\r{Fore.GREEN+Style.BRIGHT}[ Booster ] : Berhasil recharge slaps!", flush=True)
                            else:
                                print(f"\r{Fore.RED+Style.BRIGHT}[ Booster ] : Gagal recharge slaps!", flush=True)
                            energyLeft = requests.get(ProfileUrl, headers=profile_headers).json().get('energyLeft')
                        if energyLeft > 10:
                            print(f"\r{Fore.GREEN+Style.BRIGHT}[ Slap ] : Energy masih tersedia, slap lagi", flush=True)
                            continue
                        else:
                            print(f"\r{Fore.RED+Style.BRIGHT}[ Slap ] : Energy Habis", flush=True)
                            time.sleep(5)
                            profile_data = profile_response.json()
                            resetPayload = {
                                "amount" : 1,
                                "isTurbo" : False,
                                "startTimeStamp" : adjusted_timestamp
                            }
                            resetEnergy = requests.post(SaveClicks, headers=profile_headers, json=resetPayload)
                            profile_response = requests.get(ProfileUrl, headers=profile_headers)
                            break
                else:
                    print(f"{Fore.RED}[ Token ] : Gagal mendapatkan Token!")
            else:
                print(f"{Fore.RED}[ Token ] : Gagal Login!")
        
        
        print(f"\n\n{Fore.CYAN+Style.BRIGHT}==============Semua akun telah diproses=================\n")

        for detik in range(300, 0, -1):
            print(f"{Fore.YELLOW}[ !!!!!!!!!! ] : Slap ulang dalam {detik} detik", end="\r", flush=True)
            time.sleep(1)
        print(f"{Fore.YELLOW}[ !!!!!!!!!! ] : Slap ulang dalam 0 detik", end="\r", flush=True)
        print("\n")
        akun = 1
                        

if __name__ == '__main__':
    main()
import requests
from collections import Counter

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'


def get_friends(friends):
    ages = []
    for f in friends:
        if 'bdate' not in f or ('bdate' in f and len(f['bdate'].split('.')) < 3):
            continue
        bdate = int(f['bdate'].split('.')[2])
        age = 2018 - bdate
        ages.append(age)
    counter = Counter(ages).items()
    return sorted(counter, key=lambda x: (x[1], -x[0]), reverse=True)


def calc_age(uid):
    user_resp = requests.get(f'https://api.vk.com/method/users.get?v=5.71&access_token={ACCESS_TOKEN}&user_ids={uid}')
    user_id = user_resp.json()['response'][0]['id']
    friends_resp = requests.get(f'https://api.vk.com/method/friends.get?v=5.71&access_token={ACCESS_TOKEN}'
                                f'&user_id={user_id}&fields=bdate')
    result = get_friends(friends_resp.json()['response']['items'])
    return result


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)

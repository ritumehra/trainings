import sys
import getpass
import requests
import egnyte

USAGE = '''
1. TEST_USAGE_1
2. TEST_USAGE_2
3. TEST_USAGE_3
4. TEST_USAGE_4
'''

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))

try:
    if len(sys.argv) <= 1:
        sys.exit()
    else:
        mode = sys.argv[1]
        print(mode)

        username = input("Username: ").strip()
        password = getpass.getpass("Password: ").strip()
        domain = input("Domain: ").strip()

        data = {'client_id': 'cq2hfa6gzzzgy29fddkg64jm', 'username': username, 'password': password,
                'grant_type': 'password'}
        access_token = requests.post('https://' + domain + '.egnyte.com/puboauth/token', data=data).json()[
            'access_token']

        print("Access Token:", access_token)
        client = egnyte.EgnyteClient({"domain": domain + ".egnyte.com", "access_token": access_token})
        fs_api = 'https://' + domain + '.egnyte.com/pubapi/v1/fs'


except:
    print ('')
    print(sys.stderr, USAGE)
    sys.exit()

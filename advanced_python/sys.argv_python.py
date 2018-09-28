import sys
import getpass
import requests
import egnyte

USAGE = '''
Please pass a valid argument to the script 

USAGE : <script_name> <filename> <mode> <type>
'''

# url: https://egnytesupportteam.egnyte.com
# username: egnytesupportteam
# password: egnyte$upportteam

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))

try:
    if len(sys.argv) <= 1:
        sys.exit()
    else:
        execute_script = sys.argv[1]
        print(execute_script)

        if execute_script:
            username = input("Username: ").strip()
            password = getpass.getpass("Password: ").strip()
            domain = input("Domain: ").strip()

            data = {'client_id': 'cq2hfa6gzzzgy29fddkg64jm', 'username': username, 'password': password,
                    'grant_type': 'password'}

            res = requests.post('https://' + domain + '.egnyte.com/puboauth/token', data=data)
            print("Response Json:: ",res.json())
            print("Response Json:: ", res.json()['access_token'])
            access_token = requests.post('https://' + domain + '.egnyte.com/puboauth/token', data=data).json()[
                'access_token']

            print("Access Token:", access_token)
            client = egnyte.EgnyteClient({"domain": domain + ".egnyte.com", "access_token": access_token})
            fs_api = 'https://' + domain + '.egnyte.com/pubapi/v1/fs'
        else:
            print("Get the permissions to execute the script....")

except:
    print ('')
    print(sys.stderr, USAGE)
    sys.exit()

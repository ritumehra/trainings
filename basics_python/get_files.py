import egnyte
import urllib
import requests
import json
import getpass
import codecs
import sys
from datetime import datetime
from requests.utils import requote_uri

username = input("Username: ").strip()
password = getpass.getpass("Password: ").strip()
domain = input("Domain: ").strip()
folder_path = input("Folder path to search (i.e. /Shared/Documents): ").strip()
user_restrict = input("Enter username(s). Separate multiple users by comma (i.e. jbrown, asmith): ")
restrict_date = input("Restrict search by date (i.e. YYYY-MM-DD): ").strip()

# url: https://egnytesupportteam.egnyte.com
# username: egnytesupportteam
# password: egnyte$upportteam
# folder path: Shared/test_training

if user_restrict == '' or restrict_date == '':
    # print >> sys.stderr, 'Search Date or User list cannot be empty. Please run the script again and give Username(s) and Date input when asked.'
    sys.exit()
else:
    user_restrict = user_restrict.replace(' ', '').split(',')
    restrict_date = datetime.strptime(restrict_date, '%Y-%m-%d')

data = {'client_id': 'cq2hfa6gzzzgy29fddkg64jm', 'username': username, 'password': password, 'grant_type': 'password'}
get_access_token = requests.post('https://'+domain+'.egnyte.com/puboauth/token', data=data)
access_token = get_access_token.json()['access_token']
fs_api = 'https://'+domain+'.egnyte.com/pubapi/v1/fs'
client = egnyte.EgnyteClient({"domain": domain+".egnyte.com", "access_token": access_token})

def recursive_folder(path):
    try:

        uri = fs_api + path

        folder = client.GET(requote_uri(uri))
        # folder = client.GET(fs_api + urllib.quote(path.encode('utf8')))
        folder_attributes = folder.json()

        # if folder_attributes.has_key('files'):
        if "files" in folder_attributes:
            print(type(folder_attributes['files']))
            print("\n ****************** FILES FOUND ******************\n")
            print(folder_attributes['files'])
            print("\n****************** FILES FOUND ENDED ******************\n")

            for f in folder_attributes['files']:
                versions = f['num_versions']
                file_path = f['path']
                uploaded_by = f['uploaded_by']
                modified_date = datetime.strptime(f['last_modified'][5:16], '%d %b %Y')

                if versions > 1 and uploaded_by in user_restrict and modified_date == restrict_date:
                    with codecs.open('files_to_delete.txt', 'ab', 'utf8') as fout:
                        fout.write('%s\n' %file_path)
                        
    		#with codecs.open('data.log', 'ab', 'utf-8') as log:
    		    #log.write('{Path: %s, Uploaded_by: %s, last_modified: %s, num_versions: %s}\n' %(file_path, uploaded_by, f['last_modified'], versions))

        # if folder_attributes.has_key('folders'):
        if 'folders' in folder_attributes:

            print("\n****************** FOLDERS FOUND ******************\n")
            print(folder_attributes['folders'])
            print("\n****************** FOLDERS FOUND ENDED ******************\n")
            for dirs in folder_attributes['folders']:
                print ('Walking through: ' + dirs['path'])
                recursive_folder(dirs['path'])
    except Exception as e:
        print ('Error on path: %s' %path)
        with open('error.txt', 'ab') as error:
            error.write('%s\t %r\n' %(path, e))
            
    print ("\nPlease look at 'files_to_delete.txt' for the files found. You may also look at error.txt for any errors")
        
'''
This function works as well, but I using the one above that makes use of "egnyte" module

def recursive_folder_1(path):
    header = {"Authorization": "Bearer %s" %access_token}
    try:
        folder = requests.get(fs_api + urllib.quote(path.encode('utf8')), headers=header)
        folder_attributes = folder.json()

        if folder_attributes.has_key('files'):
            for f in folder_attributes['files']:
                versions = f['num_versions']
                file_path = f['path']
                uploaded_by = f['uploaded_by']
                modified_date = datetime.strptime(f['last_modified'][5:16], '%d %b %Y')

                if versions > 1 and uploaded_by in restrict_users: and modified_date == restrict_date:
                    with codecs.open('files_to_delete.txt', 'ab', 'utf8') as fout:
                        fout.write('%s\n' %file_path)

        if folder_attributes.has_key('folders'):
            for dirs in folder_attributes['folders']:
                print 'Walking through: ' + dirs['path']
                recursive_folder_1(dirs['path'])
    except Exception as e:
        print 'Error on path: %s' %path
        with open('error.txt', 'ab') as error:
            error.write('%s\t %r' %(path, e))
'''

recursive_folder(folder_path)

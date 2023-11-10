# password = 'hazf-tqaq-lwlf-wtyh'

from pyicloud import PyiCloudService
from pyicloud.exceptions import PyiCloudFailedLoginException, PyiCloudNoDevicesException
from datetime import datetime, timedelta

username = 'kapahgaiii7@yandex.ru'
password = 'F4ck_Army'

try:
    api = PyiCloudService(username, password)

    if api.requires_2fa:
        print("Two-factor authentication required.")
        code = input("Enter the code you received of one of your \
                    approved devices: ")
        result = api.validate_2fa_code(code)
        print("Code validation result: %s" % result)

        if not result:
            print("Failed to verify security code")
            exit(1)

        if not api.is_trusted_session:
            print("Session is not trusted. Requesting trust...")
            result = api.trust_session()
            print("Session trust result %s" % result)

            if not result:
                print("Failed to request trust. You will likely be \
                    prompted for the code again in the coming weeks")

    events = api.calendar.events()

    for event in events:
        print(event['title'])
        
except PyiCloudFailedLoginException:
    print("Failed login to iCloud.")
except PyiCloudNoDevicesException:
    print("No devices found.")

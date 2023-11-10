# password = 'hazf-tqaq-lwlf-wtyh'

from pyicloud import PyiCloudService
from pyicloud.exceptions import PyiCloudFailedLoginException, PyiCloudNoDevicesException
from datetime import datetime, timedelta, date, time

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
                
    start_date = date.today() + timedelta(-(date.today().day) + 1)
    print("All events from: ", start_date)
    print("Till today (inclusive):", date.today())

    calendar_service = api.calendar
    events = calendar_service.get_events(from_dt = start_date, to_dt=datetime.now(), as_objs=True)

    for event in events:
        print("Дата: ", event.startDate[3], ".", event.startDate[2],". Имя: ", event.title, sep="")

    event_count = dict()

    for event in events:
        if event.title in event_count:
            new_value = event_count[event.title]
            if event.duration == 120:
                event_count[event.title] = new_value + 2
            elif event.duration == 90:
                event_count[event.title] = new_value + 1.5
            else:
                event_count[event.title] = new_value + 1
        else:
            if event.duration == 120:
                event_count[event.title] = 2
            elif event.duration == 90:
                event_count[event.title] = 1.5
            else:
                event_count[event.title] = 1
    
    print()
    for key, value in event_count.items():
        print(value, ": ", key, sep="")
    
except PyiCloudFailedLoginException:
    print("Failed login to iCloud.")
except PyiCloudNoDevicesException:
    print("No devices found.")

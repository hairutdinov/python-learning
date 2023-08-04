import os
import sys
from datetime import datetime
from subprocess import call
import json

backup_list = []

with os.scandir('.') as entries:
    for entry in entries:
        backup_dict = {}
        modify_time = os.path.getmtime(entry.path)
        modify_date = datetime.fromtimestamp(modify_time)

        backup_dict['path'] = entry.name
        backup_dict['created'] = datetime.fromtimestamp(os.path.getctime(entry.path)).__str__()
        backup_dict['modified'] = modify_date.__str__()

        command = 'SetFile -d "%s" "%s"' % (modify_date.strftime('%m/%d/%Y %H:%M:%S'), entry.path)
        backup_dict['command'] = command

        # call(command, shell=True)

        backup_list.append(backup_dict)

print(backup_list)

log_file = 'change_creation_backup_{datetime}.json'.format(datetime=datetime.now().strftime('%Y%m%d_%H%M%S'))

json.dump(
    backup_list,
    fp=open(log_file, 'w'),
    indent=4
)

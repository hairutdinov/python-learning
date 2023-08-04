from datetime import datetime

PYCOND_DATE = datetime(year=2023, month=8, day=20, hour=8)
countdown = PYCOND_DATE - datetime.now()

print(f'Countdown to PyCon US 2023: {countdown}')
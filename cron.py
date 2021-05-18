from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='cd /home/nathan/RPi_Projects && $(which python3) /home/nathan/RPi_Projects/main.py')
job.minute.every(10)

cron.write()

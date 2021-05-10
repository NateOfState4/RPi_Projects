from crontab import CronTab

cron = CronTab(user='nathan')
job = cron.new(command='main.py')
job.minute.every(5)

cron.write()

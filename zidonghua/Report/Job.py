import schedule
import time
import subprocess


def job():
    # 这里的命令可以是执行Python脚本，或者其他你想定时执行的命令
    subprocess.run([r"D:\Users\Renrui\PycharmProjects\pythonProject\venv\Scripts\python.exe",
                    r"D:\Users\Renrui\PycharmProjects\pythonProject\venv\zidonghua\Report\JianCe.py"])

# 安排任务每10分钟执行一次
schedule.every(180).minutes.do(job)

while True:
    # 运行所有可以运行的任务
    schedule.run_pending()
    time.sleep(1)
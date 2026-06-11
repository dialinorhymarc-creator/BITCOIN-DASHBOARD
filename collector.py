import time
import subprocess

while True:

    subprocess.run(
        ["python", "fetch_data.py"]
    )

    print("Waiting 10 seconds...")

    time.sleep(10)
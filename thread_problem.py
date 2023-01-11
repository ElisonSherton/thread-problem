from threading import Thread
from datetime import datetime
import time

with open("output.txt", "w") as f:
    def compute_mean(processing_time):
        time.sleep(processing_time)
        f.writelines(f"Done mean computation at {datetime.now()}\n")
        return 1

    def compute_standard_deviation(processing_time):
        time.sleep(processing_time)
        f.writelines(f"Done median computation at {datetime.now()}\n")
        return 1

    for i in range(100):
        t_mean = Thread(target = compute_mean, args = (5, ))
        t_stdv = Thread(target = compute_standard_deviation, args = (5, ))

        t_mean.start()
        t_stdv.start()

        t_stdv.join()
        t_mean.join()
        f.writelines("\n")
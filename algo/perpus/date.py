import datetime
import json

def waktu():
    global waktu_skr
    global dld

    now = datetime.datetime.now().strftime("%Y/%m/%d")
    deadline = now + datetime.timedelta(weeks=1)
    

    # Menampilkan waktu sekarang
    waktu_skr = now.date()
    # Menampilkan waktu deadline
    dld = deadline.date()

    return waktu_skr, dld

waktu()

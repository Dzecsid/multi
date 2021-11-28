import concurrent.futures
from hashlib import md5
from random import choice

i = 0
with concurrent.futures.ProcessPoolExecutor(max_workers = 100) as executor:
    while i <= 5:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            i = i + 1
            print(s, h)
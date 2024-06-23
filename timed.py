import time
import matplotlib.pyplot as plt
from naive import naive_find
from KMP import KMP_find
from RK import RK_find
from naive2 import N


results_naive = []
results_naive2 = []
results_KMP = []
results_RK = []

with open('pan-tadeusz.txt', 'r') as file:
    data = file.read()

data2 = data.split()

for n in range(1,11):
    curr_pattern = ""
    curr_data = data2[:100*n]
    for word in curr_data:
        curr_pattern += word
        curr_pattern += " "
    curr_pattern = curr_pattern[:-1]
    start = time.perf_counter()
    naive_find(curr_pattern, data)
    stop = time.perf_counter()
    results_naive.append(stop-start)

    start = time.perf_counter()
    N(curr_pattern, data)
    stop = time.perf_counter()
    results_naive2.append(stop-start)

    start = time.perf_counter()
    KMP_find(curr_pattern, data)
    stop = time.perf_counter()
    results_KMP.append(stop-start)

    start = time.perf_counter()
    RK_find(curr_pattern, data)
    stop = time.perf_counter()
    results_RK.append(stop-start)

n = [i for i in range(100, 1001, 100)]
plt.plot(n, results_naive, label="naive")
plt.plot(n, results_naive2, label="naive2")
plt.plot(n, results_KMP, label="KMP")
plt.plot(n, results_RK, label="RK")

plt.legend()
plt.xlabel("n")
plt.ylabel("t")
plt.savefig("plot.png")

plt.show()
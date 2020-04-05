from sklearn.cluster import KMeans
import numpy as np


def get_key():
    TRACE_FILENAME = 'ptrace.trc'

    with open(TRACE_FILENAME, 'r') as f:
        lines = f.readlines()

    samples = [[float(line)] for line in lines]

    kmeans_digitalize = KMeans(n_clusters=2, random_state=0).fit(np.array(samples))
    clustered_samples = kmeans_digitalize.labels_

    low_label = kmeans_digitalize.predict([[min(samples)[0]]])[0]
    high_label = kmeans_digitalize.predict([[max(samples)[0]]])[0]

    current_state = clustered_samples[0]
    counter = 0
    aggregated_samples = []
    for e in clustered_samples:
        if current_state == e:
            counter += 1
        else:
            aggregated_samples.append((counter, current_state))
            current_state = e
            counter = 1

    #  It seems like 50 for low, 75 for square, 50 for multiply

    high_voltages = [[sample[0]] for sample in aggregated_samples if sample[1] == high_label]

    kmeans_decide_10 = KMeans(n_clusters=2, random_state=0).fit(np.array(high_voltages))

    short_interval_label = kmeans_decide_10.predict([[min(high_voltages)[0]]])
    long_interval_label = kmeans_decide_10.predict([[max(high_voltages)[0]]])

    number = ['0' if label == short_interval_label else '1' for label in kmeans_decide_10.labels_]
    # print(aggregated_samples)
    # print(''.join(number))
    return int(''.join(number), 2)


def get_cyphertext_and_n():
    TEXT_FILENAME = 'ptrace_input.txt'

    with open(TEXT_FILENAME, 'r') as f:
        cyphertext = f.readline()
        n = f.readline()

    return int(cyphertext, 16), int(n, 16)


c, n = get_cyphertext_and_n()
d = get_key()

m = pow(c, d, n)

m = bytearray.fromhex(hex(m)[2:]).decode()
print(m)

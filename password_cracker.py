import hashlib

def crack_sha1_hash(hash, use_salts = False):
    passwords = open('top-10000-passwords.txt')
    pass_list = []
    for line in passwords:
      pass_list.append(line.strip())
    passwords.close()

    if use_salts: 
      salts = open('known-salts.txt')
      salt_list = []
      for line in salts:
        salt_list.append(line.strip())
      salts.close()
    else: salt_list = ['']

    for salt in salt_list:
      for password in pass_list:

        for counter in range(2):
          h = hashlib.sha1()
          if counter == 0: h.update((salt+password).encode())
          if counter == 1: h.update((password+salt).encode())
          if h.hexdigest() == hash: 
            print('Password found:', password)
            return password

    return 'PASSWORD NOT IN DATABASE'

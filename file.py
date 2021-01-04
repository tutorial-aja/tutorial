import os,sys,time
logo = '''
 _____      _             _       _
|_   _|   _| |_ ___  _ __(_) __ _| |
  | || | | | __/ _ \| '__| |/ _` | |
  | || |_| | || (_) | |  | | (_| | | upload file
  |_| \__,_|\__\___/|_|  |_|\__,_|_| ke Github $_$
'''
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.09)
os.system('clear')
print logo
jalan('[!] dan seperti itulah cara upload file ke github')


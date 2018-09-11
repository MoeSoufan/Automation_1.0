import subprocess
#
# def get_ping():
    # command = 'ping -n 1 zombie.circlecvi.com | FIND "TTL="'
    # p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # print p.communicate()[0]

command = 'ping -l 50000 zombie.circlecvi.com -t -R'
# p = Popen([command, test], shell=True, stdout=PIPE)
p = subprocess.Popen(command, stdout=subprocess.PIPE)

for line in p.stdout:
    #print line
    if "time" in line:
        print line
# print p.communicate()

    # return

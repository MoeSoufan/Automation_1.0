import get_pid
import subprocess
import ping


pid = get_pid.getpid()
ping.get_ping()

command = 'tasklist /fi "pid eq %s"' % pid
call = subprocess.check_output(command)

print "Memory Usage: ", call.split()[-2]


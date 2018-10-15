import sys
import traceback


#  flag values
#   1000 - Login time
def print_timing(flag, var, filename):

    f = open(filename, 'a+')
    f.write('%d, %.2f\n' % (flag, var))
    f.close()

    return


def print_error(filename):
    f = open(filename, 'a+')
    f.write('ERROR, %s\n' % traceback.format_exc())
    f.close()

    return


def print_to_file(flag, filename):

    f = open(filename, 'a+')
    f.write('%d, PASS\n' % flag)
    f.close()

    return

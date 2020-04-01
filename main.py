import sys, os
import util

args = sys.argv[1:]

if args:
    util.data = util.load()
    flag = args[0]
    if flag == '-n' or flag == '--new':
        if len(args) < 2:
            util.error(1)
        elif len(args) < 3:
            util.error(2)
        elif util.exist(args[1]):
            util.error(8, args[1])
        else:
            util.opt_new(args[1], args[2])
    elif flag == '-o' or flag == '--open':
        if len(args) < 2:
            util.error(1)
        elif not util.exist(args[1]):
            util.error(7, args[1])
        else:
            util.opt_open(args[1])
    elif flag == '-i' or flag == '--info':
        if len(args) < 2:
            util.error(1)
        elif not util.exist(args[1]):
            util.error(7, args[1])
        else:
            util.opt_info(args[1])
    elif flag == '-l' or flag == '--list':
        util.opt_list()
    elif flag == '-m' or flag == '--modify':
        if len(args) < 2:
            util.error(4)
        elif len(args) < 3:
            util.error(1)
        elif len(args) < 4:
            util.error(3)
        elif not util.exist(args[2]):
            util.error(7, args[2])
        else:
            util.opt_modify(args[1], args[2], args[3])
    elif flag == '-d' or flag == '--delete':
        if len(args) < 2:
            util.error(1)
        elif not util.exist(args[1]):
            util.error(7, args[1])
        else:
            util.opt_delete(args[1])
    else:
        util.error(6, args[0])
    util.save(util.data)
else:
    print(util.usage)

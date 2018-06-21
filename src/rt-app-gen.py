#!/usr/bin/python

import argparse
import json
from RtAppGen import RtAppGen, PeriodicTask

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--task",
                    help="create task with given parameters",
                    action="append",
                    type=str)

args = parser.parse_args()
#print(args)

rag = RtAppGen()

counter = 0
for a in args.task:
	arg_task_s = a.split(':')
	'''
	print(arg_task_s)
	print("Runtime: {}".format(arg_task[0]))
	print("Deadline: {}".format(arg_task[1]))
	print("Period: {}".format(arg_task[2]))
	print(new_task)
	'''
	try:
		new_task = PeriodicTask('t_{}'.format(counter),
		                        (int)(arg_task_s[0]),
		                        (int)(arg_task_s[1]),
		                        (int)(arg_task_s[1]),
		                        arg_task_s[2])
	except NameError as e:
		print "Task generation error: {}".format(e)
		exit(-1)


	rag.addTask(new_task)

	counter = counter + 1

print(json.dumps(rag.generate(), sort_keys=True, indent=4))

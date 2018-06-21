def schedClassFullName(short):
	if short == 'r':
		return "SCHED_RR"
	if short == 'd':
		return "SCHED_DEADLINE"
	if short == 'o':
		return "SCHED_OTHER"
	return -1

class GenericTask(object):
	def __init__(self):
		self.name = ''
		self.ds = {}

	def __str__(self):
		return "Task {} : {}".format(self.name, self.ds)


class PeriodicTask(GenericTask):
	def __init__(self, name, runtime, deadline, period, sched_class='o'):
		super(PeriodicTask, self).__init__()

		if schedClassFullName(sched_class) == -1:
			raise NameError('"{}" is not a valid policy'.format(sched_class))

		self.name = name
		self.ds['runtime'] = runtime
		self.ds['deadline'] = deadline
		self.ds['period'] = period
		self.ds['sched_class'] = schedClassFullName(sched_class)

class RtAppGen:
	tasks = []
	common = {}

	def __init__(self, duration=-1, calibration="CPU0", sched_class="o"):
		if schedClassFullName(sched_class) == -1:
			raise NameError('"{}" is not a valid policy'.format(sched_class))

		self.tasks = []
		self.common['duration'] = duration
		self.common['calibration'] = calibration
		self.common['default_policy'] = schedClassFullName(sched_class)

	def addTask(self, task):
		self.tasks.append(task)

	def __str__(self):
		return "Number of tasks: {}".format(len(self.tasks))

	def generate(self):
		ds = {}
		ds['global'] = self.common
		ds['tasks'] = {}
		for t in self.tasks:
			ds['tasks'][t.name] = t.ds

		return ds

import os
import sys
import json
import platform
import site


class Ppm():

	def __init__(self):

		self.system = platform.system()

		self.reserved_words = ['add', 'install', 'init']

		# Listing the current directory
		self.current_directory = os.listdir('.')

		self.activate_this = './python_modules/bin/activate_this.py'

		if 'ppm.json' in self.current_directory:

			with open('ppm.json', 'r') as f:

				self.data = json.loads(f.read())
				f.close()

		try:
			import virtualenv

		except ModuleNotFoundError:

			os.system('pip install --user virtualenv')

	def init(self):
		'''
			Initialize a new python project in current directory.
		'''
		
		result = 1
		# Creating ppm environment
		if 'python_modules' not in self.current_directory:

			result = os.system('python -m virtualenv python_modules')

		if result == 0 and 'ppm.json' not in self.current_directory:

			# Creating the settings structure
			self.data = {
				'project_version': str(input('project version: ')),
				'scripts': {
					'start': f'./python_modules/bin/python {str(input("type your entry point (example --> main.py): "))}'
				},
				'dependencies': [

				]
			}

			# Save the settings in a file
			with open('ppm.json', 'w') as f:
				
				f.write(json.dumps(self.data, indent=4))
				f.close()

	def install(self):
		'''
			This function installs dependencies listed in ppm.json
		'''

		# Call pip in ppm environment to install the dependencies.
		to_run = './python_modules/bin/pip install '

		if 'python_modules' not in self.current_directory:

			self.init()

		# Getting all dependencies
		for package in self.data['dependencies']:

			to_run += f'{package} '
		# Run the pip.
		os.system(to_run)

	def add(self, packages):
		'''
			This function install new dependencies of your project.
		'''

		to_install = ''

		for package in packages:

			to_install += f'{package} '

		# Install dependencies
		result = os.system(f'./python_modules/bin/pip install {to_install}')

		# Check if the installation went well
		if result == 0:

			# Save the dependencies in data attribute.
			for package in packages:

				# Check if this package already is not in list
				if package not in self.data['dependencies']:

					self.data['dependencies'].append(package)

			# Save the dependencies in a file
			with open('ppm.json', 'w') as f:

				f.write(json.dumps(self.data, indent=4))
				f.close()
	
	def execute_script(self, script):
		'''
			This function run script in data['scripts']
		'''

		try:

			# Open the file that active the ppm environment.
			with open(self.activate_this, 'r') as f:

				# Close this file
				f.close()

			# Get the script to run.
			to_execute = self.data['scripts'][script]

			# Run the script
			os.system(to_execute)

		except KeyError:

			print('type a valid script')


if __name__ == '__main__':

	ppm = Ppm()

	if len(sys.argv) > 1:
		
		if sys.argv[1] not in ppm.reserved_words:

			ppm.execute_script(sys.argv[1])

		else:

			if sys.argv[1] == 'init':

				ppm.init()

			elif sys.argv[1] == 'install':

				ppm.install()

			elif sys.argv[1] == 'add':

				ppm.add(sys.argv[2:])
					
	else:

		print('Insufficient arguments!')

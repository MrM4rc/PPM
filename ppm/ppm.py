import os
import sys
import json
import platform
import site


class Ppm():

	def __init__(self):

		self.system = platform.system()

		self.reserved_words = ['add', 'install', 'remove', 'init', 'gen']

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
				'name': str(input('Project name: ')),
				'author': str(input('Author: ')),
				'email': str(input('Email: ')),
				'description': str(input('Short description: ')),
				'github': str(input('Project url on github: ')),
				'project_version': str(input('project version: ')),
				'scripts': {
					'start': f'./python_modules/bin/python {str(input("type your entry point (example --> main.py): "))}'
				},
				'dependencies': [

				]
			}

			# Save the settings in a file
			self.save()
			
	def save(self):

		with open('ppm.json', 'w') as file:

			file.write(json.dumps(self.data, indent=4))
			file.close()

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

	def gen(self, typ):
		'''
			Generate requirements and setup.py files
		'''
		
		if typ == 'req':

			text = ''

			with open('requirements.txt', 'w') as file:

				for dependencie in self.data['dependencies']:

					text += dependencie + '\n'

				file.write(text)
				file.close()

		elif typ == 'setup':

			text = '''import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="$1", # Replace with your own username
	version="$2",
	author="$3",
	author_email="$4",
	description="$5",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="$6",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)
'''
			with open('setup.py', 'w') as file:

				text = text.replace('$1', self.data['name'])
				text = text.replace('$2', self.data['project_version'])
				text = text.replace('$3', self.data['author'])
				text = text.replace('$4', self.data['email'])
				text = text.replace('$5', self.data['description'])
				text = text.replace('$6', self.data['github'])

				file.write(text)
				file.close()

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

			# Save the new dependencies
			self.save()
	
	def remove(self, package_name):

		if package_name in self.data['dependencies']:

			self.data['dependencies'].remove(package_name)

			os.system(f'./python_modules/bin/pip uninstall {package_name}')
			self.save()

		else:

			print('Dependencie not found')
	
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

			if len(sys.argv) > 2:

				for argument in sys.argv[2:]:

					to_execute += f' {argument}'

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

			elif sys.argv[1] == 'gen':

				ppm.gen(sys.argv[2])

			elif sys.argv[1] == 'remove':

				ppm.remove(sys.argv[2])
					
	else:

		print('Insufficient arguments!')

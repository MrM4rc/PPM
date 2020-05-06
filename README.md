# Python package manager (PPM)

<p>Python package manager is a software to manage your dependencies.</p>

## How to use

<p><b>with python:</b></p>

<p>creating new project</p>

```bash
python ppm.py init
```

<p>a ppm.json json file will be created and all project settings will be stored</p>

<p>adding new dependencies</p>

```bash
python ppm.py add flake8 jedi PyFiFinder
```
<p>all dependencies installed will be in ppm.json</p>
<p>if python_modules is deleted, enough run ppm install to all dependencies be installed.</p>

### how to run your scripts?

<p>ppm is similar the npm and yarn, to call your script, type in terminal:</P>

```bash
python ppm.py start
```
<p>to add new scripts, edit script area in ppm.json</p>

```json
{
    "project_version": "1.0",
    "scripts": {
		"start": "./python_modules/bin/python main.py",
		"command": "./python_modules/bin/python your_script.py"
    },
    "dependencies": [
        "flake8",
        "jedi",
        "PyFiFinder"
    ]
}
```

<p><b>Using a binary:</b></p>

<p>download binary file in: <a href='#'>link</a></p>

<p>After place the binary in '/home/user/.local/bin'</p>

<p>now you can call ppm without call python</p>

```bash
ppm init
ppm add flake8 jedi PyFiFinder
ppm start
```

## generating setup and requirements files

<p>Using the ppm is possible generate requirements.txt and setup.py files of automatic may.</p>

```bash
ppm gen req
ppm gen setup
```


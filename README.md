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

### how to run my scripts?

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
		// add new scripts here
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

<p>copy the binary file in output and put in /home/$USER/.local/bin/</p>

<p>now you can call ppm without call python</p>

```bash
ppm init
ppm add flake8 jedi PyFiFinder
ppm start
```

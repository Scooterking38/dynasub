import subprocess, sys, os, inspect

_this_dir = os.path.dirname(os.path.abspath(__file__))

for frame in inspect.stack():
    caller = os.path.abspath(frame[1])
    if os.path.isfile(caller) and not caller.startswith(_this_dir):
        break

if not os.environ.get('DYNASUB'):
    env = os.environ.copy()
    env['DYNASUB'] = '1'
    existing = [os.path.abspath(p) for p in env.get('PYTHONPATH', '').split(os.pathsep) if p]
    env['PYTHONPATH'] = os.pathsep.join([os.path.dirname(caller)] + existing)
    result = subprocess.run([sys.executable, '-m', 'dynasub', caller], env=env)
    sys.exit(result.returncode)

import os
for module in os.listdir(os.path.dirname(__file__)):
    if module in ['__init__.py', 'config.py'] or module[-3:] != '.py':
        continue
    __import__(module[:-3], locals(), globals())
del module

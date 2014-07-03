from setuptools import setup


setup(
    name="Fap Folder Creator",
    version="1.0",
    py_modules=['ffc'],
    install_requires=[
        'Click',
        'Haul',
    ],
    entry_points='''
        [console_scripts]
        hello=hello:main
    ''',
)
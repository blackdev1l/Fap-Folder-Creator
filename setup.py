from setuptools import setup


setup(
    name="Fap Folder Creator",
    version="0.3",
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
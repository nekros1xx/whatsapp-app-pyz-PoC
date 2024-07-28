from setuptools import setup

setup(
    name="calc_executer",
    version="1.0",
    py_modules=["run_calc"],
    entry_points={
        'console_scripts': [
            'calc_executer=run_calc:main',
        ],
    },
)


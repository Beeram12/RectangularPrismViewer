from setuptools import setup, find_packages

setup(
    name='RectangularPrismViewer',
    version='0.1.0',
    description='A GUI application for visualizing and calculating properties of rectangular prisms.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Beeram12/RectangularPrismViewer',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: LINUX',
    ],
    python_requires='>=3.10',
    install_requires=[
        'python',
        'pip',
        'numpy==2.1.2',
        'pyqt>=5.15.0',
        'pyqt5-sip',
        'pythonocc-core'
    ],
    entry_points={
        'console_scripts': [
            'prism-calculator=main:main',
        ],
    },
)

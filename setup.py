from setuptools import setup

setup(
    name='document_filler',
    version='1.0',
    packages=['src', 'build'],
    entry_points={
        'console_scripts': [
            'document_filler = src.main:main',
            'build_document_filler = build.build_exe:build_executable'
        ]
    },
    install_requires=[
        'python-docx',
        'pyinstaller'
        'argparse'
    ]
)
from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='mqtt_bundle',
    packages=['mqtt_bundle'],
    version='2.3',
    description='mqtt support for applauncher',
    author='Alvaro Garcia Gomez',
    author_email='maxpowel@gmail.com',
    url='https://github.com/applauncher-team/mqtt_bundle',
    download_url='https://github.com/applauncher-team/mqtt_bundle/archive/master.zip',
    keywords=['applauncher', 'bundle', 'mqtt'],
    classifiers=['Topic :: Adaptive Technologies', 'Topic :: Software Development', 'Topic :: System',
                 'Topic :: Utilities'],
    install_requires=install_requires
)

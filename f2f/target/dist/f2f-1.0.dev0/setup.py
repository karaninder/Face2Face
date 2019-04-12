#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'f2f',
        version = '1.0.dev0',
        description = '',
        long_description = '',
        author = '',
        author_email = '',
        license = '',
        url = '',
        scripts = [
            'scripts/generate_train_data.py',
            'scripts/reduce_model.py',
            'scripts/pix2pix.py',
            'scripts/environment.yml',
            'scripts/fc1.py',
            'scripts/process.py',
            'scripts/freeze_model.py',
            'scripts/run_webcam.py',
            'scripts/scp.py',
            'scripts/split.py'
        ],
        packages = [],
        namespace_packages = [],
        py_modules = [
            'generate_train_data',
            'reduce_model',
            'pix2pix',
            'fc1',
            'process',
            'freeze_model',
            'run_webcam',
            'scp',
            'split'
        ],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '',
        obsoletes = [],
    )

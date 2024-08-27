rm -rf dist
python setup.py sdist
pip install ./dist/zdppy_log-0.1.0.tar.gz
#!flask/bin/python
from app import app
app.secret_key = 'dev_test_demo_key'
app.config.from_object('config')
app.run(debug=True)

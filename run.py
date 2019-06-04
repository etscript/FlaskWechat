__author__ = 'Ran'
#!/usr/bin/env python
from apps import app, blueprint

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True, threaded=True)
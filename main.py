from app import *
from flask import Flask




if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)







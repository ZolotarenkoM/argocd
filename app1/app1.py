 #!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    myfile = open("page.html", mode='r')
    page   = myfile.read()
    myfile.close()
    return page


#--------Main------------------
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

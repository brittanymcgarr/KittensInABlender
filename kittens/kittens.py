################################################################################
## Kittens in a Blender Demo                                                  ##
## The only blending game for kittens.                                        ##
################################################################################

from flask import Flask, render_template

# initialize the Flask app
app = Flask(__name__)


# create the home route
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


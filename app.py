from flask import Flask
from flask import jsonify
import rahmah_makan_vision

app = Flask(__name__)

@app.route('/api/fridges')
def index():

    objects_num, labels, img, bnd_box, cnfdce = rahmah_makan_vision.get_objects_num_with_labels()

    return jsonify(
        objects_num = objects_num,
        labels = labels
    )


if __name__ == '__main__':
    #debug=True doesn't require you to run the code with every change
    app.run(debug=True)

Steps to run the flask sever

1. Install all required libraries

```
pip install flask
pip install opencv-python tensorflow
pip install cvlib

```

2. Specify the route you want flask to serve

```
@app.route('/your-route-goes-here')

```

3. Overview
    - The client makes a request to the flask app
    - Hazem's vision module is run
    - The result is sent back to the client in JSON
    - If we are using multiple webcams then, the client can also specify camera number, otherwise all fridges   will have the same camera

```
@app.route('/')
def index():

    objects_num, labels, img, bnd_box, cnfdce = rahmah_makan_vision.get_objects_num_with_labels()

    return jsonify(
        objects_num = objects_num,
        labels = labels
    )

```

4. Once all steps are done, run app.py, go to the browser and type in localhost:<port_number>/api/fridges
from flask import Flask , render_template, request
import tensorflow as tf
from keras.preprocessing import image as IMAGE


app = Flask(__name__)
MODEL = tf.keras.models.load_model("C:/Users/WIN/Desktop/cat-vs-dog-main/models/catVSdog.h5")


def predict(img):
        img = IMAGE.load_img(img, target_size=(256, 256))
        image = IMAGE.img_to_array(img)
        image = image.reshape(-1, 256,256,3)
        pred = MODEL.predict(image)[0]
        if pred==0:
            result = "cat"
        else:
            result = "dog"
        return result


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload",methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        img = request.files['file']
        img.save("uploads/up_img.jpg")
        if img:
            return predict("uploads/up_img.jpg")


if __name__ == "__main__":
    app.run(debug = True)

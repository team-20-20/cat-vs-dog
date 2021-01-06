import tensorflow as tf
from tensorflow.keras.preprocessing import image
from flask import Flask,request,render_template,redirect,url_for

MODEL = tf.keras.models.load_model("models/catVSdog.h5")
app = Flask(__name__)


def predict(img):
        img = tf.keras.preprocessing.image.load_img(img, target_size=(256, 256))
        image = tf.keras.preprocessing.image.img_to_array(img)
        image = image.reshape(-1, 256,256,3)
        pred = MODEL.predict(image)[0]
        if pred>0.5:
            res = "dog"
        else:
            res = "cat"
        if res == "cat":
            return render_template("predicted.html", result="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRV5oPLKyxF_Tz0tXpxbJuTTBD1rtxuBfVVtg&usqp=CAU",name=res.upper())
        else:
            return render_template("predicted.html", result="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcSPkUi4U7rR6eLI_aCynt_FlqBkzlmE0NfrKmZlexrH3Xqz_igN0qOZxgACsWrf9aTzaNMJ8Oi-lmICtdvTppY5HzsmIDAbUzRw&usqp=CAU&ec=45750088",name=res.upper())


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

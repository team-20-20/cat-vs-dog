from flask import Flask , render_template, request
app = Flask(__name__)

@app.route("/")
def home():


	return render_template("index.html")
@app.route("/upload",methods=["POST", "GET"])
def upload():
	if request.method == "POST":
		image = request.files['file']

		if image:
			return 'file uploaded successfully'
		



if __name__ == "__main__":
	app.run(debug = True)

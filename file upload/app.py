import os


from flask import Flask, request, render_template, send_from_directory,redirect, url_for

__author__ = 'Siddhesh'

app = Flask(__name__)



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/upload")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    # return send_from_directory("images", filename, as_attachment=True)
    # return render_template("gallery.html", image_name=filename)
    return redirect(url_for('get_gallery'))

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route('/del_image/<filename>',methods=['POST'])
def del_image(filename):
    path = os.path.join(APP_ROOT, 'images/'+filename)
    print(path)
    os.remove(path)
    print("%s has been removed successfully" %filename)
    return redirect(url_for('get_gallery'))


@app.route('/')
def get_gallery():
    image_names = os.listdir('./images')
    print(image_names)
    return render_template("gallery.html", image_names=image_names)

if __name__ == "__main__":
    app.run(port=4555, debug=True)



import os,shutil


from flask import Flask, request, render_template, send_from_directory,redirect, url_for,abort
import cv2

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


@app.route("/download")
def downloader():
    return render_template("download.html")

app.config["CLIENT_IMAGES"]=APP_ROOT + '\\extracted_photos'
@app.route('/download/<path:path>',methods = ['GET','POST'])
def download(path):
    """Download a file."""
    try:
        return send_from_directory(app.config["CLIENT_IMAGES"], path, as_attachment=True)
    except FileNotFoundError:
        abort(404)
    # return send_from_directory("images", filename, as_attachment=True)
    # return render_template("gallery.html", image_name=filename)
    # return redirect(url_for('get_gallery'))


@app.route("/grp_uploader")
def grp_upload():
    return render_template("grp_uploader.html")

@app.route("/grp_uploader", methods=["POST"])
def grp_uploader():
    target = os.path.join(APP_ROOT, 'group_of_images/')

    for filename in os.listdir(target):
        file_path = os.path.join(target, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

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
    # imagelist = os.listdir('./group_of_images')
    # for image in imagelist:
    #     pdf.add_page()
    #     pdf.image(image,x,y,w,h)
    # pdf.output("yourfile.pdf", "F")
    target=os.path.join(APP_ROOT, 'data_generator.py')
    target1=os.path.join(APP_ROOT, 'model_data/deploy.prototxt')
    target2=os.path.join(APP_ROOT, 'model_data/weights.caffemodel')
    open(target1, 'r',errors="ignore").read()
    open(target2, 'r',errors="ignore").read()
    file = open(target, 'r',errors="ignore").read()
    exec(file)
    # return send_from_directory("images", filename, as_attachment=True)
    # return render_template("gallery.html", image_name=filename)
    return redirect(url_for('query_uploader'))

@app.route("/query_uploader")
def query_upload():
    return render_template("query_uploader.html")

@app.route("/query_uploader", methods=["POST"])
def query_uploader():
    target = os.path.join(APP_ROOT, 'query/')

    for filename in os.listdir(target):
        file_path = os.path.join(target, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

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
    target1=os.path.join(APP_ROOT, 'model_data/deploy.prototxt')
    target2=os.path.join(APP_ROOT, 'model_data/weights.caffemodel')
    target3=os.path.join(APP_ROOT, 'face_extractor.py')
    target4=os.path.join(APP_ROOT, 'facematching.py')
    open(target1, 'r',errors="ignore").read()
    open(target2, 'r',errors="ignore").read()
    file = open(target3, 'r',errors="ignore").read()
    exec(file)
    file = open(target4, 'r',errors="ignore").read()
    exec(file)
    # return send_from_directory("images", filename, as_attachment=True)
    # return render_template("gallery.html", image_name=filename)
    return redirect(url_for('downloader'))

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

if __name__ == '__main__':
    app.debug = True
    app.run()
from flask import Flask, request, jsonify, render_template
import os
from preprocess_model.parsing_pdf import document_parser


app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    file = file = request.files['file']
    output = document_parser(file)
    return output
    # if 'file' not in request.files:
    #     return jsonify(error="No file part"), 400
    # file = request.files['file']
    # if file.filename == '':
    #     return jsonify(error="No selected file"), 400
    # if file and allowed_file(file.filename):
    #     filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    #     file.save(filename)
    #     return jsonify(success=True, message="File uploaded successfully"), 200
    # else:
    #     return jsonify(error="Invalid file type"), 400

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
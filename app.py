from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message=None)

@app.route('/index.html')
def index():
    return render_template('index.html', message=None)

@app.route('/tables.html')
def tables():
    return render_template('tables.html', message=None)


@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file:
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)
        message = 'Archivo subido con éxito.'
        return render_template('index.html', message=message)
    message = 'Error al subir el archivo.'
    return render_template('index.html', message=message)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)

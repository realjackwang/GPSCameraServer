
from flask import Flask
from flask import request
from flask import Response
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test', methods=['POST'])
def test():
    value = request.form['test']
    print(value)
    return 'Hello, this is GPSCameraServer, we had just received your message, good luck!'


@app.route('/file/<filename>', methods=['GET'])
def file_download(filename):
    def send_chunk():  # 流式读取
        store_path = './upload/%s' % filename
        with open(store_path, 'rb') as target_file:
            while True:
                chunk = target_file.read(20 * 1024 * 1024)  # 每次读取20M
                if not chunk:
                    break
                yield chunk
    response = Response(send_chunk(), content_type='application/octet-stream')
    response.content_length = os.path.getsize('./upload/%s' % filename)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

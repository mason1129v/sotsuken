from flask import Flask, render_template, request, Response

import cv2, os

app = Flask(__name__)
app.debug = True
print(os.getcwd())

@app.route('/index.html')
def main():
    return render_template('index.html')

@app.route('/get_send', methods=['GET'])
def doGet():
    return '{}:{}'.format(request.method, request.args.get('date', ''))


if __name__ = '__main__':
    app.run()
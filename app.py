from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['video_url']
    file_name = request.form['file_name']

    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()
    video.download(filename=file_name)

    return 'Descarga completada'

if __name__ == '__main__':
    app.run()

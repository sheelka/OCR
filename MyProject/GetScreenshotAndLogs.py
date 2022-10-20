from flask import Flask,send_from_directory, send_file
import os

app = Flask(__name__)
# Specify directory to download from . . .
DOWNLOAD_DIRECTORY = "C:\\Users\\0014Q7744\\Documents\\Dissertation_Final\\Test_Images"

@app.route('/get-files/<path:path>',methods = ['GET','POST'])
def get_files(path):

    """Download a file."""
    try:
        return send_from_directory("C:\\Users\\0014Q7744\\Documents\\Dissertation_Final\\Test_Images\\", path, as_attachment=True)
    except FileNotFoundError:
        print("FileNotFound Exception")

@app.route('/get-logs/<path:path>',methods = ['GET','POST'])
def get_logs(path):
    print("here")
    """Download a file."""
    try:
        filenames = os.listdir("C:\\Users\\0014Q7744\\Documents\\Dissertation_Final\\Logs")
        print(filenames)
        for file in filenames:
            print(file)
            if path+".txt" == file:
                print("matched")
                return send_file("C:\\Users\\0014Q7744\\Documents\\Dissertation_Final\\Logs\\"+file)
    except FileNotFoundError:
        print("FileNotFound Exception")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000, threaded = True, debug = True)
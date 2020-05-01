from flask import Flask ,render_template ,url_for,request,redirect,jsonify
import os
import module1  
import glob
import time
from werkzeug.utils import secure_filename
import speech_recognition as sr
r = sr.Recognizer()
 

app = Flask(__name__)
#app.config["AUDIO_UPLOAD"] = "C:\Users\dipen\Desktop\pythonproject\audio"
@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        f = request.files['file']
        f.save(secure_filename(f.filename))
        time.sleep(2)
        filename = glob.glob("*.wav")[0]
        print(f)
        module1.sound = filename
        #sound=filename
        text=module1.main()
        print(text)
        os.remove(filename)
        return 'file uploaded successfully'

    return render_template('ff.html')
    
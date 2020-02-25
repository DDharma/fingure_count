#import deepndency
from cv2 import cv2
import os,sys,time,operator
import numpy as np 
from keras.models import model_from_json
from keras import backend as k 
from flask import Flask,render_template,request

#creating Flask instences
app = Flask(__name__)

#creating root location
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Category these are all cattegories for prediction
categories = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE'}
#creating routes
@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload",methods=["POST","GET"])
def upload():
    target = os.path.join(APP_ROOT,"images/")
    print(target)

    #creating directory in its not avalible
    if not os.path.isdir(target):
        os.mkdir(target)
    

    #uploading the file
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        print("file_name",filename)
        destination = "/".join([target,filename])
        print(destination)
        file.save(destination)


        # Loading the model from json file 
        k.clear_session()
        json_file = open("model-bw.json", "r")
        model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(model_json)
        # load weights into new model
        loaded_model.load_weights("model-bw.h5")
        print("Loaded model from disk")

        #loading the image
        roi = cv2.imread(destination)
            
        # Resizing the ROI so it can be fed to the model for prediction
        roi = cv2.resize(roi, (64, 64)) 
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        cv2.imshow("test", test_image)
        # Batch of 1
        result = loaded_model.predict(test_image.reshape(1, 64, 64, 1))
        prediction = {'ZERO': result[0][0], 
                    'ONE': result[0][1], 
                    'TWO': result[0][2],
                    'THREE': result[0][3],
                    'FOUR': result[0][4],
                    'FIVE': result[0][5]}
        # Sorting based on top prediction
        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
            
        # Displaying the predictions in console
        print("Predection",prediction[0][0])
        k.clear_session()
        cv2.destroyAllWindows()
        chosen_img = "Chosen image is "+prediction[0][0]
    return chosen_img

#runnig the server
if __name__ =="__main__":
    app.run(debug=True,port=8002)
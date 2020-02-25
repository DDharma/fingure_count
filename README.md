# This made for task given by Avanov Solutions by intersala


## Question: Create a flask application, upload the image and run any ml model to analyse the image and show response back.


## Function of program:
    Its predict the fingure upto 5 fingure when we upload the image file from any directory in our system.

## Working:
    1.I train the mode using cnn and save the model in json format file name as "model-bw.json"
    2.Now using this model I predict the images (the sample image are shown in directory "sample_images"
    3.If I run file "app.py" the is crete the server on local host on port no "8002"
    4.If i click on chose button then system directory files system are open then I chose the image file and when I click on the predict       button the selected image is save in directory called "images" with tha same name of selected image previous name and predict the image
    5.Then open again same url and do from step 1 to 4 for further prediction.

## Note: 
    1.PLese select image from directory "sample_image" for prediction
    2.For windows user run the "install.bat" file for installing all dependency 
    3.If you not windows please install following dependency
        a.keras
        b.opencv 4.0 and above
        c.numpy
        d.flask


    

# Rating Prediction


## Test
To test the prediction model you need to run the bash script `run.sh` which
creates the **FLASK_APP** environment variable and creates a python flask server api.
After that you'll need to open the file web/index.html

## Alternative test
An alternative to using the website interface is using the linux command curl, the following command should work

`curl -H "Content-Type: text/plain" -X POST -d "I love this dress" http://localhost:5000/api`

# Directories
- **api/:** contains the flask server code
- **data:** contains the dataset, pretrained model and sample dataframe
- **src:** contains a jupyter notebook with the experimentation, training and testing
- **web:** contains the source code for the html page

## Requirements
```
numpy
pandas
scikit-learn
nltk
regex
joblib
flask
flask-cors
```

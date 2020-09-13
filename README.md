# Rating Prediction


## Usage
1. Install required dependencies 
2. Run the bash script `run.sh` which creates the FLASK_APP environment variable and creates a python flask server api
3. Open the web interface `web/index.html`
4. (Optional) Instead of using the web interface use the curl command `curl -H "Content-Type: text/plain" -X POST -d "I love this dress" http://localhost:5000/api`


# Directories
- **api/:** contains the flask server code
- **data/:** contains the dataset, pretrained model and sample dataframe
- **src/:** contains a jupyter notebook with the experimentation, training and testing
- **web/:** contains the source code for the html page

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
matplotlib
```

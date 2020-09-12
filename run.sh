!/usr/bin/bash
echo Creating server at http://127.0.0.1:5000
echo To test the ratings predictor open the file web/index.html in your browser
export FLASK_APP=server.py && cd api/ && python -m flask run &

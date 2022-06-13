# ML-Predictor
This is the ML path repository for Locasee, a Google Bangkit product capstone that helps businesses to choose their operational location.
## How to replicate
- Clone our project
- You can follow our flow on the locasee.ipynb, and directly run each of the cell
- Run the server.py
- Access the endpoint from the consumer (in this case, it's the android side), it''ll be like http://localhost:5000/classify?nearest_office=0.2&nearest_school=0.3 with JSON ouput as {"prediction": "A"}

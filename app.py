from flask import Flask, render_template, request
# import os
from utils.prediction import predict_json


app = Flask(__name__)
app.config['DEBUG'] = True

gcp_project = "model-almanac-291915"
model_cooing = "COOLING_MODEL_GCP"
model_heating = "EMRE_HEATING_MODEL_GCP"


app.route("/index")
def hello():
    return "Welcome to Energy Consumption Application!!"

# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         return render_template('index.html')
#     elif request.method == 'POST':
#         new_data = [{'X1': float(request.form["relative_compactness"]), 
#                     'X2': float(request.form["surface_area"]), 
#                     'X3': float(request.form["wall_area"]), 
#                     'X4': float(request.form["roof_area"]), 
#                     'X5': float(request.form["overall_height"]), 
#                     'X6': float(request.form["orientation"]),
#                     'X7': float(request.form["glazing_area"]), 
#                     'X8': float(request.form["glazing_area_dist"])}]
#         heating_load = predict_json(gcp_project, model_heating, new_data, version="v1")
#         cooling_load = predict_json(gcp_project, model_cooing, new_data, version="v1")
#         return render_template('prediction.html', 
#                                 new_data=new_data, 
#                                 heating_load=round(heating_load[0]["predicted_Y1"][0], 1),
#                                 cooling_load=round(cooling_load[0]["predicted_Y2"][0], 1))
#     else:
#         return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
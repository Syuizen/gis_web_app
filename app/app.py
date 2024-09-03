from flask import Flask, request, render_template, jsonify, send_from_directory
import os
import json
import geopandas as gpd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'geojson'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    if file and allowed_file(file.filename):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        # Perform regression analysis
        gdf = gpd.read_file(filepath)
        if 'avg_epc' in gdf.columns and 'avg_price' in gdf.columns:
            X = gdf[['avg_epc']].values.reshape(-1, 1)  # Feature matrix
            y = gdf['avg_price'].values  # Response vector
            model = LinearRegression()
            model.fit(X, y)
            beta = model.coef_[0]
            intercept = model.intercept_
        else:
            beta = None
            intercept = None
        
        return jsonify({
            "success": "File uploaded successfully",
            "filename": file.filename,
            "beta": beta,
            "intercept": intercept
        })
    
    return jsonify({"error": "Invalid file type"})


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

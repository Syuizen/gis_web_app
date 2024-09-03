# GIS-Based Web Application

## Overview

This project is a GIS-based web application that allows users to upload geospatial data files (e.g., GeoJSON) and visualize the data on an interactive map. The application is built using Flask for the backend and Leaflet.js for the client-side map rendering. It also includes a basic regression analysis on the uploaded geospatial data, specifically analyzing the relationship between `avg_price` and `avg_epc`.

## Features

- **Upload Geospatial Data**: Users can upload GeoJSON files containing geospatial data.
- **Map Visualization**: Visualize geospatial data on a Leaflet map with different color scales for `avg_epc` and `avg_price`.
- **Layer Control**: Toggle between different data layers (`avg_epc` and `avg_price`) on the map.
- **Regression Analysis**: Perform a simple linear regression on the uploaded data to compute the relationship between `avg_price` and `avg_epc`.
- **Dynamic User Interface**: Display regression results and allow interactive map exploration directly in the web browser.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Dependencies

Install the following Python packages:

- Flask
- GeoPandas
- Scikit-Learn
- Leaflet.js (included via CDN in HTML)
- Chroma.js (included via CDN in HTML)

You can install the required Python packages using pip:

```bash
pip install flask geopandas scikit-learn
```

## Project Structure

```
gis_web_app/
│
├── app.py                  # Main Flask application
├── uploads/                # Directory to store uploaded files
├── templates/
│   └── index.html          # HTML template for the web interface
└── README.md               # Project README file
```

## Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/syuizen/gis_web_app.git
   cd gis_web_app
   ```

2. **Install Dependencies**:

   Install the required Python packages:

   ```bash
   pip install flask geopandas scikit-learn
   ```

3. **Run the Flask Application**:

   Start the Flask development server:

   ```bash
   python app.py
   ```

   By default, the application will run on `http://127.0.0.1:5000/`.

4. **Open the Application in a Web Browser**:

   Go to `http://127.0.0.1:5000/` to access the application.

5. **Upload a GeoJSON File**:

   - Click the "Choose File" button to select a GeoJSON file from your computer.
   - Click the "Upload" button to upload the file.
   - The map will dynamically display the uploaded geospatial data.

6. **Visualize Data and Regression Results**:

   - Toggle between the `avg_epc` and `avg_price` layers using the layer control on the map.
   - View the regression results displayed below the file upload form.

## Regression Analysis

The application performs a simple linear regression analysis on the uploaded geospatial data to compute the relationship between `avg_price` and `avg_epc`. The regression model is based on the formula:

\[
\text{avg\_price} = \beta \times \text{avg\_epc} + \text{intercept}
\]

The computed values of `beta` and `intercept` are displayed on the web interface after a successful file upload.

## Notes

- Ensure that the uploaded GeoJSON files contain the properties `avg_epc` and `avg_price` for the regression analysis and color scales to work correctly.
- The application currently supports only GeoJSON files for upload and visualization.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework for Python
- [Leaflet.js](https://leafletjs.com/) - JavaScript library for interactive maps
- [GeoPandas](https://geopandas.org/) - Python library for geospatial data
- [Scikit-Learn](https://scikit-learn.org/) - Python machine learning library
- [Chroma.js](https://gka.github.io/chroma.js/) - JavaScript library for color scales


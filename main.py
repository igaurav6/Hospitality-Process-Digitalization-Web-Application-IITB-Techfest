from flask import Flask, request, jsonify, send_file
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload_groups', methods=['POST'])
def upload_groups():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, 'groups.csv')
    file.save(filepath)
    return jsonify({"message": "Groups file uploaded successfully."})

@app.route('/upload_hostels', methods=['POST'])
def upload_hostels():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, 'hostels.csv')
    file.save(filepath)
    return jsonify({"message": "Hostels file uploaded successfully."})

@app.route('/allocate_rooms', methods=['GET'])
def allocate_rooms():
    groups_df = pd.read_csv(os.path.join(UPLOAD_FOLDER, 'groups.csv'))
    hostels_df = pd.read_csv(os.path.join(UPLOAD_FOLDER, 'hostels.csv'))
    
    # Implement allocation logic here
    # ...

    # Save the result to a new CSV file
    output_filepath = os.path.join(UPLOAD_FOLDER, 'allocation.csv')
    allocation_df.to_csv(output_filepath, index=False)
    
    return send_file(output_filepath, as_attachment=True, download_name='allocation.csv')

if __name__ == '__main__':
    app.run(debug=True)

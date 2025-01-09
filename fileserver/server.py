from flask import Flask, request, send_from_directory, jsonify
	import os
	
	app = Flask(__name__)
	UPLOAD_FOLDER = './uploads'
	os.makedirs(UPLOAD_FOLDER, exist_ok=True)
	
	app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
	
	@app.route('/')
	def index():
		return jsonify({"message": "Welcome to the File Sharing Server!"})
		
	# Route to upload files
	@app.route('/upload', method=['POST'])
	def upload_file():
		if 'file' not in request.files:
			return jsonify({"error": "No file part"}), 400
		file = request.files['file']
		if file.filename == '':
			return jsonify({"error": "No selected file"}), 400
		file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
		file.save(file_path)
		return jsonify({"message": "File uploaded successfully", "filename": file.filename}), 200
		
	# Route to download files
	@app.route('/download/<filename>', methods=['GET'])
	def download_file(filename):
		return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
		
	# Route to list all files
	@app.route('/files', method=['GET'])
	def list_files():
		files = os.listdir(app.config['UPLOAD_FOLDER'])
		return jsonify({"files":files}),200
		
	if __name__ == '__main__':
		app.run(debug=True)
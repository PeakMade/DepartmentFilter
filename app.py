"""
Simple Test App for Remote Authentication Service
Just serves a static HTML page - no backend logic needed
"""

from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """Serve the test frontend"""
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🔐 Authentication Test App")
    print("="*60)
    print("\n💡 Open http://localhost:5050 in your browser")
    print("\n🎯 Testing: https://peakauth-rg.calmcliff-d4a82c7d.eastus.azurecontainerapps.io")
    print("="*60 + "\n")
    
    app.run(debug=True, port=5050)

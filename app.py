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
    import os
    port = int(os.environ.get('PORT', 5050))
    print("\n" + "="*60)
    print("🔐 Authentication Test App")
    print("="*60)
    print(f"\n💡 Running on port {port}")
    print("\n🎯 Testing: https://peakauth-rg.calmcliff-d4a82c7d.eastus.azurecontainerapps.io")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=port, debug=False)

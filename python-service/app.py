from flask import Flask, request, redirect
import os

app = Flask(__name__)

def get_referrer_base():
    """Extracts the referring service's base URL from the request"""
    referrer = request.referrer
    if referrer:
        # Extract base URL from referrer (e.g., "http://35.88.92.227:8080")
        return referrer.split('/api/')[0] if '/api/' in referrer else referrer
    # Fallback to Java service if no referrer (direct access)
    return f"http://{request.host.split(':')[0]}:8080"

@app.route('/api/python')
def home():
    home_url = get_referrer_base()
    python_base_url = request.url_root.rstrip('/')
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <!-- [Keep all your existing head content] -->
    <body>
        <h1>🚀 Hello from Python Service! 🚀</h1>
        <div class="button-container">
            <a href='{home_url}' class='service-link'>Back to Home</a>
            <button class='button' onclick='window.location.href="{python_base_url}/api/python/health"'>Check Health</button>
        </div>
    </body>
    </html>
    """

@app.route('/api/python/health')
def health():
    home_url = get_referrer_base()
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <!-- [Keep all your existing head content] -->
    <body>
        <h1>🚀 Service Health Status 🚀</h1>
        <div class="status">✅ All Systems Operational</div>
        <a href="{home_url}" class="service-link">Back to Home</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
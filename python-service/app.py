from flask import Flask, request
import os

app = Flask(__name__)

def get_referrer_base():
    """Extracts the referring service's base URL from the request"""
    referrer = request.referrer
    if referrer:
        # If the Python service URL was called via /api/python, remove everything after /api/
        return referrer.split('/api/')[0] if '/api/' in referrer else referrer
    # If no referrer, fallback to root of this service
    return request.host_url.rstrip('/')

@app.route('/api/python')
def home():
    home_url = get_referrer_base()
    python_base_url = request.url_root.rstrip('/')

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Python Service</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
            }}
            .button-container {{
                margin-top: 20px;
            }}
            .service-link, .button {{
                display: inline-block;
                margin: 10px;
                padding: 10px 20px;
                text-decoration: none;
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                border: none;
                cursor: pointer;
            }}
            .button:hover, .service-link:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
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
    python_base_url = request.url_root.rstrip('/')

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Health Status</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
            }}
            .status {{
                font-size: 24px;
                margin-bottom: 20px;
            }}
            .service-link {{
                display: inline-block;
                padding: 10px 20px;
                text-decoration: none;
                background-color: #28a745;
                color: white;
                border-radius: 5px;
            }}
            .service-link:hover {{
                background-color: #218838;
            }}
        </style>
    </head>
    <body>
        <h1>🚀 Service Health Status 🚀</h1>
        <div class="status">✅ All Systems Operational</div>
        <a href="{home_url}" class="service-link">Back to Home</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

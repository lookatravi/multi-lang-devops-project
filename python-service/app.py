from flask import Flask, request

app = Flask(__name__)

def get_base_url():
    """Dynamically generates the base URL including correct scheme (http/https)"""
    return request.url_root.rstrip('/')

@app.route('/api/python')
def home():
    base_url = get_base_url()
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python Service</title>
        <style>
            body {{
                background: linear-gradient(to right, #d3cce3, #e9e4f0);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                flex-direction: column;
            }}
            h1 {{
                font-size: 3em;
                color: #333;
                margin-bottom: 20px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            }}
            .service-link {{
                font-size: 1.5em;
                color: #4b6cb7;
                text-decoration: none;
                padding: 12px 24px;
                border: 2px solid #4b6cb7;
                border-radius: 8px;
                transition: all 0.3s ease;
                margin: 10px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            .service-link:hover {{
                background-color: #4b6cb7;
                color: white;
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0,0,0,0.15);
            }}
            .button-container {{
                display: flex;
                gap: 20px;
                margin-top: 20px;
            }}
            .button {{
                font-size: 1.5em;
                padding: 12px 24px;
                border: 2px solid #4b6cb7;
                background-color: #4b6cb7;
                color: white;
                border-radius: 8px;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            .button:hover {{
                background-color: #3a5a9b;
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0,0,0,0.15);
            }}
        </style>
    </head>
    <body>
        <h1>🚀 Hello from Python Service! 🚀</h1>
        <div class="button-container">
            <a href='{base_url}' class='service-link'>Back to Home</a>
            <button class='button' onclick='window.location.href="{base_url}/api/python/health"'>Check Health</button>
        </div>
    </body>
    </html>
    """

@app.route('/api/python/health')
def health():
    base_url = get_base_url()
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Health Check</title>
        <style>
            body {{
                background: linear-gradient(to right, #d3cce3, #e9e4f0);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                flex-direction: column;
            }}
            h1 {{
                font-size: 3em;
                color: #333;
                margin-bottom: 20px;
            }}
            .status {{
                font-size: 1.5em;
                color: #2e7d32;
                font-weight: bold;
                margin-bottom: 30px;
                padding: 15px 30px;
                background-color: rgba(46, 125, 50, 0.1);
                border-radius: 8px;
            }}
            .service-link {{
                font-size: 1.5em;
                color: #4b6cb7;
                text-decoration: none;
                padding: 12px 24px;
                border: 2px solid #4b6cb7;
                border-radius: 8px;
                transition: all 0.3s ease;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            .service-link:hover {{
                background-color: #4b6cb7;
                color: white;
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0,0,0,0.15);
            }}
        </style>
    </head>
    <body>
        <h1>🚀 Service Health Status 🚀</h1>
        <div class="status">✅ All Systems Operational</div>
        <a href="{base_url}" class="service-link">Back to Home</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
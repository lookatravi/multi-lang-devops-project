from flask import Flask

app = Flask(__name__)

@app.route('/api/python')
def home():
    return """
    <html>
        <head>
            <style>
                body {
                    background: linear-gradient(to right, #d3cce3, #e9e4f0);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                    flex-direction: column;
                }
                h1 {
                    font-size: 3em;
                    color: #333;
                    margin-bottom: 20px;
                }
                .service-link {
                    font-size: 1.5em;
                    color: #4b6cb7;
                    text-decoration: none;
                    padding: 10px 20px;
                    border: 2px solid #4b6cb7;
                    border-radius: 5px;
                    transition: all 0.3s ease;
                }
                .service-link:hover {
                    background-color: #4b6cb7;
                    color: white;
                }
                .button {
                    font-size: 1.5em;
                    padding: 10px 20px;
                    border: 2px solid #4b6cb7;
                    background-color: #4b6cb7;
                    color: white;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: all 0.3s ease;
                }
                .button:hover {
                    background-color: #333;
                }
            </style>
        </head>
        <body>
            <h1>🚀 Hello from Python Service! 🚀</h1>
            <a href='http://localhost:8080' class='service-link'>Back to Home</a>
            <button class='button' onclick='window.location.href="/api/python/health"'>Check Health</button>
        </body>
    </html>
    """

@app.route('/api/python/health')
def health():
    return """
    <html>
        <head>
            <style>
                body {
                    background: linear-gradient(to right, #d3cce3, #e9e4f0);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                    flex-direction: column;
                }
                h1 {
                    font-size: 3em;
                    color: #333;
                    margin-bottom: 20px;
                }
                .status {
                    font-size: 1.5em;
                    color: green;
                }
                .service-link {
                    font-size: 1.5em;
                    color: #4b6cb7;
                    text-decoration: none;
                    padding: 10px 20px;
                    border: 2px solid #4b6cb7;
                    border-radius: 5px;
                    transition: all 0.3s ease;
                }
                .service-link:hover {
                    background-color: #4b6cb7;
                    color: white;
                }
            </style>
        </head>
        <body>
            <h1>🚀 Health Check 🚀</h1>
            <div class="status">Health: OK</div>
            <a href="http://localhost:8080" class="service-link">Back to Home</a>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

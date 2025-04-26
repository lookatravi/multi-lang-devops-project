package main

import (
	"fmt"
	"net/http"
)

func hello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, `
		<html>
		<head>
			<title>Go Service</title>
			<style>
				body {
					background: linear-gradient(135deg, #f5f5dc, #e0e0e0);
					display: flex;
					justify-content: center;
					align-items: center;
					height: 100vh;
					margin: 0;
					font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
					flex-direction: column;
				}
				h1 {
					color: #333;
					font-size: 48px;
					animation: float 3s ease-in-out infinite;
					margin-bottom: 20px;
				}
				@keyframes float {
					0%, 100% { transform: translateY(0); }
					50% { transform: translateY(-20px); }
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
			<h1>Hello from Go Service! 🚀</h1>
			<a href='javascript:history.back()' class='service-link'>Back to Home</a>
		</body>
		</html>
	`)
}

func main() {
	http.HandleFunc("/api/go", hello)
	http.ListenAndServe(":5002", nil)
}
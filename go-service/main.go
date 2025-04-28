package main

import (
	"fmt"
	"net/http"
)

func htmlTemplate(title, content string, showHealthLink bool, r *http.Request) string {
	baseURL := getBaseURL(r)
	healthLink := ""
	if showHealthLink {
		healthLink = fmt.Sprintf(`<a href='%s/api/go/health' class='service-link'>Health Check</a>`, baseURL)
	}
	
	return fmt.Sprintf(`
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
			.content {
				font-size: 1.2em;
				margin-bottom: 30px;
				max-width: 600px;
				text-align: center;
			}
			@keyframes float {
				0%%, 100%% { transform: translateY(0); }
				50%% { transform: translateY(-20px); }
			}
			.link-container {
				display: flex;
				gap: 20px;
				flex-wrap: wrap;
				justify-content: center;
			}
			.service-link {
				font-size: 1.2em;
				color: #4b6cb7;
				text-decoration: none;
				padding: 10px 20px;
				border: 2px solid #4b6cb7;
				border-radius: 5px;
				transition: all 0.3s ease;
				margin: 5px;
			}
			.service-link:hover {
				background-color: #4b6cb7;
				color: white;
			}
			.health-status {
				color: #2e7d32;
				font-weight: bold;
			}
		</style>
	</head>
	<body>
		<h1>%s</h1>
		<div class="content">%s</div>
		<div class="link-container">
			<a href='%s' class='service-link'>Back to Home</a>
			<a href='javascript:history.back()' class='service-link'>Back to Previous Page</a>
			%s
		</div>
	</body>
	</html>
	`, title, content, baseURL, healthLink)
}

func getBaseURL(r *http.Request) string {
	scheme := "http"
	if r.TLS != nil {
		scheme = "https"
	}
	return fmt.Sprintf("%s://%s", scheme, r.Host)
}

func hello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, htmlTemplate(
		"Hello from Go Service! 🚀",
		"This is the Go backend service running on port 5002",
		true, // Show Health Check link
		r,
	))
}

func health(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, htmlTemplate(
		"Go Service Health Check",
		"✅ Status: <span class='health-status'>OK</span> - Service is running smoothly!",
		false, // Don't show Health Check link on health page
		r,
	))
}

func main() {
	http.HandleFunc("/api/go", hello)
	http.HandleFunc("/api/go/health", health)
	fmt.Println("Go service running on port 5002")
	http.ListenAndServe(":5002", nil)
}
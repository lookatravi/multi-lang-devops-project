# Build Stage
FROM golang:1.16-alpine AS builder

WORKDIR /app

COPY go.mod ./
COPY . .

RUN go build -o go-service .

# Final Image
FROM alpine:latest

WORKDIR /root/

COPY --from=builder /app/go-service .

EXPOSE 5002

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:5002/api/go || exit 1

CMD ["./go-service"]

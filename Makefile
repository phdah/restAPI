IMAGE=rest-api:latest

install:
	docker build --network host -t $(IMAGE) .

start:
	docker run --network host -p 80:80 $(IMAGE) &

stop:
	docker kill $$(docker ps -q -f "ancestor=$(IMAGE)")
curl:
	curl -X POST 'http://localhost:5000/app?name=Johan' \
	-H 'Authorization: Bearer phdah' \
	-H 'Content-Type: application/json' \
	-d '{"database": "db", "schema": "dbt"}'

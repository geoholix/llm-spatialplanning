run:
	uvicorn src.main:app --reload

lint:
	flake8 src

format:
	black src

test:
	pytest tests

.PHONY: test run docker
test:
	python -m unittest discover -s tests -v
run:
	python -m src.ml_eval_lab --rows 3000 --seed 42 --output-dir artifacts
docker:
	docker build -t ml-reliability-lab .
	docker run --rm ml-reliability-lab

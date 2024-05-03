start:
	python -m uvicorn app:app --host 0.0.0.0 --port 3500 --reload

stop:
	-kill -9 `lsof -t -i:3500` 2> /dev/null
app:
	python -m uvicorn app:app --host 0.0.0.0 --port 3000 --reload

stop:
	-kill -9 `lsof -t -i:3000` 2> /dev/null
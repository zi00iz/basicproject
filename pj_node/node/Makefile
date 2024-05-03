start:
	uvicorn app:app --host 0.0.0.0 --port 8500 --reload

stop:
	-kill -9 `lsof -t -i:8500` 2> /dev/null

from multiprocessing import cpu_count

wsgi_app = "fastapi_simple_template.main:app"
worker_class = "uvicorn.workers.UvicornWorker"
bind = "0.0.0.0:80"
workers = cpu_count() * 2 + 1

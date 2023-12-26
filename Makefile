start:
	python3 manage.py

create_migration:
	@read -p "Enter migration message: " message; \
	alembic revision --autogenerate -m "$$message"

upgrade:
	@read -p "Enter revision: " revision; \
	alembic upgrade "$$revision"

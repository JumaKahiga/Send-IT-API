from app import create_app
from app.api.database import db


app = create_app()


@app.cli.command()
def migrate():
	""" Creates tables based on create_tables method in database.py . """
	db.create_tables()


@app.cli.command()
def destroy():
	""" Drops tables based on drop_table method in database.py . """
	db.drop_tables()

if __name__ == '__main__':
	app.run(debug=True)
from app import app
from . import calvertjournal


@app.route('/calvertjournal')
def calvert_journal():
    return calvertjournal.index()

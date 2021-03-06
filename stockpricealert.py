from appPkg import create_app, db
from appPkg.models import Stock, User, alertTracker

app = create_app() 

if __name__ == '__main__':
   app.run(host="localhost", port=int("5000")) # Only needed for Spyder debug

# Environment: 'flask shell'
# Other commands: flask routes
@app.shell_context_processor
def make_shell_context():
    """
    Registers functions for DB to be imported into shell environment
    
    Usage:
        $ flask shell
        >>> db
        >>> Stock
        >>> alertTracker

    Returns
    -------
    dict
        Database models for easy query and lookup via Python shell.

    """
    return {'db': db, 'Stock': Stock, 'User': User, 'alertTracker': alertTracker}
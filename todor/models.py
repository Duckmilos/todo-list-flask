from todor import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __init__(self ,username, password):
       
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)
    state = db.Column(db.Boolean, default=False)

    def __init__(self ,title, description, state=False):
        self.title = title
        self.description = description
        self.state = state
        self.created_by = self.created_by
    def __repr__(self):
        return f'<Todo {self.title}>'
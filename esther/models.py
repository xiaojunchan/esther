from esther import db, bcrypt


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True, nullable=False)
    full_name = db.Column(db.String(128))
    short_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, email, short_name, full_name=None, password=None,
                 is_active=True, is_admin=False):
        self.email = email
        self.short_name = short_name
        self.full_name = full_name
        self.is_active = is_active
        self.is_admin = is_admin

        if password is not None:
            self.set_password(password)

    def __unicode__(self):
        return u'<User {0}>'.format(self.email)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

from database import db
from database import app




app.app_context().push()
db.create_all()
from database import id
admin=id(id_pic="1")
db.session.add(admin)
db.session.commit()

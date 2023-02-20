from server import ma


# ESQUEMA DE USUÁRIOS USANDO ORM Marshmallow
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email')


# ESQUEMA DE TAREFAS USANDO ORM Marshmallow
class NoteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content')

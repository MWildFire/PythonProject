from peewee import *

conn = PostgresqlDatabase('apps',
                          host='c-c9qos3e3p7k6g7nl5g0e.rw.mdb.yandexcloud.net',
                          port=6432,
                          user='u2',
                          password='golovachlena2970',
                          sslmode='require',
                          sslrootcert='/Users/mvstrike/.postgresql/root.crt'
                        )

cursor = conn.cursor()
class BaseModel(Model):
    class Meta:
        database = conn  # соединение с базой, из шаблона выше


class User(BaseModel):
    user_id = AutoField(column_name='id', primary_key=True)
    email = TextField(column_name='email', null=True)
    username = TextField(column_name='username', null=True)
    password = TextField(column_name='password', null=True)

    class Meta:
        table_name = 'users'

# Получение user'а по параметру
user = User.get(User.email == 'mvstrike17@gmail.com')
print('user: ', user.user_id, user.email, user.password)

# Добавление user'а
user = User(email='mvstrike17@gmail.com', username='mvstrike', password='12345678')
user.save()

conn.close()
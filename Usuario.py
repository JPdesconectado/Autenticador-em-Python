from SQLite import Sqlite

class Usuarios(object):

    def __init__(self, idusuario = 0, usuario = "", passhash = "", sal = ""):
        self.info = {}
        self.idusuario = idusuario
        self.usuario = usuario
        self.passhash = passhash
        self.sal = sal


    def insertUser(self):

        banco = Sqlite()

        try:

            c = banco.conexao.cursor()
            c.execute("""insert into usuarios (usuario, passhash, sal) values (?, ?, ?)""", (self.usuario, self.passhash, self.sal))
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"

        except:
            return "Ocorreu um erro na inserção do usuário"

    def selectUser(self, usuario):
        banco =  Sqlite()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where usuario = ?", (usuario,))

            for linha in c:
                self.passhash = linha[2]
                self.sal = linha[3]
            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"


    def selectAllUsers(self):
        banco = Sqlite()
        try:

            c = banco.conexao.cursor()

            users = c.execute("select * from usuarios").fetchall()

            for linha in c:
                self.usuario = linha[1]
                self.passhash = linha[2]
                self.sal = linha[3]
            c.close()

            return users
        except:
            return "Usuário não encontrado."

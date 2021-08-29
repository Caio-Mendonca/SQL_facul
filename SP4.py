import sqlite3

def ExcluiCliente(Cod):
  sql = """
        select Count(codigo) from cadastro
        where codigo = :param
        """

  cursor.execute(sql, {'param' : Cod})
  x = cursor.fetchone()
  print(x[0])
  if x[0] == 0:
    return "Cliente {} não Existe".format(Cod)
  else:
    sql = "delete from cadastro where codigo = :param"
    cursor.execute(sql, {'param' : Cod})
    conector.commit()
    return "Cliente {} Excluído".format(Cod)

conector = sqlite3.connect("conta.db")
cursor = conector.cursor()

ExcluiCliente(1507)

import unittest,mysql
from test.mysql_op import MysqlOp
from test.definitions import noun
class TDD_TEST_MYSQL(unittest.TestCase):
    def setUp(self):
        self.m = MysqlOp('mml',{'noun': 'VARCHAR(255)', 'meaning': 'VARCHAR(510)'})
        return super().setUp()
    def test_key(self):
        self.assertRaises(mysql.connector.errors.ProgrammingError, lambda: self.m.createPrimaryKey())
        try:
            self.m.addPrimaryKey()
        except mysql.connector.errors.ProgrammingError:
            pass
    def test_unique(self):
        self.assertIsNone(self.m.unique('noun'))
    def test_insert(self):
        val = ("Gaussian elimination", "an algorithm that performs elementary transformations to bring a system of linear equations into reduced row-echelon form")
        r=self.m.insertInto(val)
        self.assertEqual(self.m.mycursor.rowcount, 1 if r else -1)
        val =  [(k, v) for k, v in noun.items()]
        r=self.m.executemany(val)
        self.assertEqual(self.m.mycursor.rowcount, len(val) if r else - 1)
        f=self.m.where({'noun' :'Gaussian elimination'})
        self.assertEqual(self.m.mycursor.fetchall()[0][1],'an algorithm that performs elementary transformations to bring a system of linear equations into reduced row-echelon form')
    def test_insert_id(self):
        sql = "INSERT INTO mml (noun, meaning) VALUES (%s, %s)"
        val = ("B=A⊤", "For A ∈ Rm×n the matrix B ∈ Rn×m with bij =aji iscalled the transpose of A")
        self.m.insertInto( val)
        self.assertIsInstance( self.m.mycursor.lastrowid,int)
if __name__ == '__main__':
    unittest.main()

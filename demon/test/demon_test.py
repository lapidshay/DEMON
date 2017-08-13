import unittest
import demon as d
import os
import networkx as nx


class DemonTestCase(unittest.TestCase):

    def test_demon_lib(self):
        g = nx.karate_club_graph()
        nx.write_edgelist(g, "test.csv", delimiter=",")

        D = d.Demon("test.csv")
        coms = D.execute()

        self.assertEqual(len(coms), 2)

        D = d.Demon("test.csv", file_output=True)
        D.execute()

        f = open("communities.txt")
        count = 0
        for _ in f:
            count += 1
        self.assertEqual(count, 2)

        os.remove("test.csv")
        os.remove("communities.txt")

    def test_script(self):
        g = nx.karate_club_graph()
        nx.write_edgelist(g, "test.csv", delimiter=",")

        os.system("python ../Demon.py test.csv 0.25")
        f = open("communities.txt")
        count = 0
        for _ in f:
            count += 1
        self.assertEqual(count, 2)

        os.remove("test.csv")
        os.remove("communities.txt")

if __name__ == '__main__':
    unittest.main()

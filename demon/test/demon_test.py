import unittest
import demon as d
import os
import networkx as nx


class DemonTestCase(unittest.TestCase):

    def test_demon_lib(self):
        g = nx.karate_club_graph()
        nx.write_edgelist(g, "test.csv", delimiter=" ")

        D = d.Demon("test.csv", file_output=False, epsilon=0.3)
        coms = D.execute()

        self.assertEqual(len(coms), 2)

        D = d.Demon("test.csv", file_output=True, epsilon=0.3)
        D.execute()

        f = open("demon_0.3_communities.txt")
        count = 0
        for _ in f:
            count += 1
        self.assertEqual(count, 2)

        os.remove("test.csv")
        os.remove("demon_0.3_communities.txt")



if __name__ == '__main__':
    unittest.main()

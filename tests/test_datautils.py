import unittest
import popstats.datautils as du

class TestCanadaMapPlotMethods(unittest.TestCase):

    testdatapath = "../dataset/testdata.csv"
    def Test_loadall(self):
        df = du.loadall(testdatapath)
        pass
        
    def Test_loadsection(self):
        pass

    def Test_validchunk(self):
        pass

    def Test_loadprovinces(self):
        pass

if __name__ == '__main__':
    unittest.main()

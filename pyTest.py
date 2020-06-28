import sys
import os
import re
import unittest 


class Update(object):
    
    Path = os.path.join(os.environ["SourcePath"],"develop","global","src")
    assert os.path.exists(Path)
    
    def __init__(self, fileName):
        self.fName = fileName
        self.rfNamePath = os.path.join(self.Path, self.fName)
        assert os.path.exists(self.rfNamePath)
		os.chmod(self.rfNamePath, 0755)

        self.wfNamepath = self.rfNamePath + 1


    def updateSconstruct(self):
        new_file = open(self.wfNamepath, "w")
        
        with open(self.rfNamePath, "r") as rf:
            for line in rf:
                pattern=re.sub("point\=[\d]+","point="+os.environ["BuildNum"],line)
                new_file.write(pattern)

        rf.close()
        new_file.close()


    def updateVersion(self):
        new_file = open(self.wfNamepath, "w")
        
        with open(self.rfNamePath, "r") as rf:
            for line in rf:
                pattern=re.sub("ADLMSDK_VERSION_POINT\=[\d]+","ADLMSDK_VERSION_POINT="+os.environ["BuildNum"],line)
                new_file.write(pattern)
                
        rf.close()        
        new_file.close()


    def updateLatest(self):
        os.remove(self.rfNamePath)
        assert os.path.exists(self.wfNamepath)
        os.rename(self.wfNamepath, self.rfNamePath)



# Tests

class Test(unittest.TestCase):
    
    def setUp(self):
 
        self.cTest = Update('VERSION')
		#self.cTest = Update('SCONSTRUCT')
        
        
    def test_one_File(self):
        testFile = 'version'
		#testFile = 'sconstruct'
        self.assertEqual(testFile.upper(), self.cTest.fName)
        testFileOne = 'version1'
		#testFile = 'sconstruct1'
        self.assertEqual(testFileOne.upper(), self.cTest.wfName)
        
    
    def test_two_RWFilePaths(self):
        """ To check read and write file paths 
            Ex : D:\pyRefactor\develop\global\src\VERSION
        """
        assert os.path.exists(self.cTest.Path)==1
        assert os.path.exists(self.cTest.rfNamePath)==1
        assert os.path.exists(self.cTest.wfNamepath)==0
        
        
    def test_four_updateVersion(self):
        self.cTest.updateVersion()
		#self.cTest.updateSconstruct()
        
    def test_three_readFile(self):
        with open(self.cTest.rfNamePath) as rf:
            line = rf.readline()
            print ("After VERSION: %s" % (line))
            rf.seek(0, 1)
            line = rf.readline()
            print ("After VERSION: %s" % (line))
            
    
        
        
    def test_five_testupdateLatest(self):
        assert os.path.exists(self.cTest.rfNamePath)==1
        assert os.path.exists(self.cTest.wfNamepath)==1
        #self.cTest.updateLatest
       
        assert os.path.exists(self.cTest.rfNamePath)==1
        assert os.path.exists(self.cTest.wfNamepath)==0

       
   
   
   
if __name__ == "__main__":
    unittest.main()



    

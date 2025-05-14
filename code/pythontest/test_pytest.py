#encoding=utf-8
import pytest
class TestDemo:
    def test_001(self):
        print("hahahhha")
if __name__=="__main__":
    pytest.main(["-s","-v","--html=report/report.html","test_pytest.py"])
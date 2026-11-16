import os
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from main import run

class ProjectTests(unittest.TestCase):
    def setUp(self):
        os.chdir(ROOT)

    def test_representative_sample(self):
        result=run()
        expected={'first_load_applied': 3, 'rerun_applied': 0, 'stored_records': 2}
        for key,value in expected.items():
            self.assertEqual(result[key],value, f'Mismatch on {key}')

    def test_replay_consistency(self):
        self.assertEqual(run(),run())

if __name__=='__main__':
    unittest.main()

#!/usr/bin/env python2.7
import sys
import unittest
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

sys.path.append('../src')
import fastautil as fa

class TestSingleEntryFastaFile(unittest.TestCase):
    def test_seq_len(self):
        fa_file = fa.SingleEntryFastaFile('data/NC_000913_3.fna')
        self.assertEqual(fa_file.ref_seq_len, 4641652)

        tfa_fn = 'data/test_fautil1.fna'
        with open(tfa_fn, 'w') as tfa_file:
            tfa_file.write('>Test\n')
            tfa_file.write('A' * 50 + '\n')
            tfa_file.write('C' * 16 + '\n')
        test_fa_instance = fa.SingleEntryFastaFile(tfa_fn)
        self.assertEqual(test_fa_instance.ref_seq_len, 66)

    def test_get_seq(self):
        tfa_fn = 'data/test_fautil2.fna'
        with open(tfa_fn, 'w') as tfa_file:
            tfa_file.write('>Test\n')
            tfa_file.write('ACGTA' * 10 + '\n')
            tfa_file.write('C' * 16 + '\n')
        test_fa_instance = fa.SingleEntryFastaFile(tfa_fn)
        self.assertEqual(test_fa_instance.get_seq(0, 5), 'ACGTA')
        self.assertEqual(test_fa_instance.get_seq(5, 10), 'ACGTA')
        self.assertEqual(test_fa_instance.get_seq(3, 10), 'TAACGTA')
        self.assertEqual(test_fa_instance.get_seq(50, 55), 'CCCCC')
        self.assertEqual(test_fa_instance.get_seq(45, 55), 'ACGTACCCCC')


if __name__ == '__main__':
    unittest.main()


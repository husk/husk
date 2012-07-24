import os
import sys
from cStringIO import StringIO
import shutil
import unittest
from husk import HuskError
from husk.commands import init, add, remove, move, info


class CLIInitTestCase(unittest.TestCase):
    def tearDown(self):
        shutil.rmtree('.husk')

    def test_init_noargs(self):
        options = init.parser.parse_args(''.split())
        init.parser.handle_raw(options)
        self.assertTrue(os.path.exists('.husk'))
        self.assertFalse(os.path.exists('.husk/config'))

    def test_init_existing(self):
        options = init.parser.parse_args(''.split())
        init.parser.handle_raw(options)
        self.assertTrue(os.path.exists('.husk'))
        self.assertRaises(HuskError, init.parser.handle_raw, options)

    def test_init_path(self):
        options = init.parser.parse_args(os.getcwd().split())
        init.parser.handle_raw(options)
        self.assertTrue(os.path.exists('.husk'))

    def test_init_config(self):
        options = init.parser.parse_args('-d'.split())
        init.parser.handle_raw(options)
        self.assertTrue(os.path.exists('.husk/config'))


class CLIAddTestCase(unittest.TestCase):
    def test_add(self):
        options = init.parser.parse_args()
        init.parser.handle_raw(options)

        options = add.parser.parse_args('python/cli python/web'.split())
        add.parser.handle_raw(options)
        self.assertTrue(os.path.exists('python/cli/cues.md'))
        self.assertTrue(os.path.exists('python/web/summary.md'))
        shutil.rmtree('python')
        shutil.rmtree('.husk')


class CLIRemoveTestCase(unittest.TestCase):
    def test_remove(self):
        options = init.parser.parse_args()
        init.parser.handle_raw(options)

        options = add.parser.parse_args('python/cli python/web'.split())
        add.parser.handle_raw(options)

        options = remove.parser.parse_args('python/cli'.split())
        remove.parser.handle_raw(options)
        self.assertTrue(os.path.exists('python/cli'))

        options = remove.parser.parse_args('python/web -d'.split())
        remove.parser.handle_raw(options)
        self.assertFalse(os.path.exists('python/web'))

        shutil.rmtree('.husk')


class CLIMoveTestCase(unittest.TestCase):
    def test_move(self):
        options = init.parser.parse_args()
        init.parser.handle_raw(options)

        options = add.parser.parse_args('python/cli python/web'.split())
        add.parser.handle_raw(options)

        options = move.parser.parse_args('python/cli python/command-line'.split())
        move.parser.handle_raw(options)
        self.assertTrue(os.path.exists('python/command-line'))
        self.assertFalse(os.path.exists('python/cli'))

        shutil.rmtree('.husk')
        shutil.rmtree('python')


class CLIInfoTestCase(unittest.TestCase):
    def test_info(self):
        options = init.parser.parse_args()
        init.parser.handle_raw(options)

        options = add.parser.parse_args('python/cli python/web'.split())
        add.parser.handle_raw(options)

        options = info.parser.parse_args([])
        stdout = sys.stdout
        sys.stdout = StringIO()
        info.parser.handle_raw(options)
        self.assertEqual(sys.stdout.getvalue(), '2 notes\n-----\npython/cli\npython/web\n')
        sys.stdout = stdout

        shutil.rmtree('.husk')
        shutil.rmtree('python')


if __name__ == '__main__':
    unittest.main()

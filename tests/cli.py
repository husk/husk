import os
import sys
from cStringIO import StringIO
import shutil
import unittest
from husk import HuskError
from husk.commands import init, add, remove, move, info

def init_repo(*args):
    options = init.parser.parse_args(args)
    init.parser.handle_raw(options)
    return options


class BaseTestCase(unittest.TestCase):
    def tearDown(self):
        if os.path.exists('.husk'):
            shutil.rmtree('.husk')

class CLIInitTestCase(BaseTestCase):
    def test_init_noargs(self):
        init_repo()
        self.assertTrue(os.path.exists('.husk'))
        self.assertFalse(os.path.exists('.husk/config'))

    def test_init_existing(self):
        options = init_repo()
        self.assertTrue(os.path.exists('.husk'))
        self.assertRaises(HuskError, init.parser.handle_raw, options)

    def test_init_path(self):
        init_repo(os.getcwd())
        self.assertTrue(os.path.exists('.husk'))

    def test_init_config(self):
        init_repo('-d')
        self.assertTrue(os.path.exists('.husk/config'))


class CLIAddTestCase(BaseTestCase):
    def test_add(self):
        init_repo()

        options = add.parser.parse_args('python/cli python/web'.split())
        add.parser.handle_raw(options)

        self.assertTrue(os.path.exists('python/cli/cues.md'))
        self.assertTrue(os.path.exists('python/web/summary.md'))

        shutil.rmtree('python')


class CLIRemoveTestCase(BaseTestCase):
    def test_remove(self):
        init_repo()

        options = add.parser.parse_args('python/cli python/web'.split())
        add.parser.handle_raw(options)

        options = remove.parser.parse_args('python/cli'.split())
        remove.parser.handle_raw(options)
        self.assertTrue(os.path.exists('python/cli'))

        options = remove.parser.parse_args('python/web -d'.split())
        remove.parser.handle_raw(options)
        self.assertFalse(os.path.exists('python/web'))


class CLIMoveTestCase(BaseTestCase):
    def test_move(self):
        init_repo()

        options = add.parser.parse_args('python/cli python/web'.split())
        add.parser.handle_raw(options)

        options = move.parser.parse_args('python/cli python/command-line'.split())
        move.parser.handle_raw(options)
        self.assertTrue(os.path.exists('python/command-line'))
        self.assertFalse(os.path.exists('python/cli'))

        shutil.rmtree('python')


class CLIInfoTestCase(BaseTestCase):
    def test_info(self):
        init_repo()

        options = add.parser.parse_args('python/cli python/web'.split())
        add.parser.handle_raw(options)

        options = info.parser.parse_args([])
        stdout = sys.stdout
        sys.stdout = StringIO()
        info.parser.handle_raw(options)
        self.assertEqual(sys.stdout.getvalue(), '2 notes\n-----\npython/cli\npython/web\n')
        sys.stdout = stdout

        shutil.rmtree('python')


if __name__ == '__main__':
    unittest.main()

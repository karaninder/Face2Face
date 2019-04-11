import ast
import tokenize

from sys import stdin

__version__ = '1.3'

PYTEST_ERROR_CODE = 'T003'
PYTEST_ERROR_MESSAGE = 'use of Django-style assert statement found (instead of regular assert)'
ASSERTS = ('assertAlmostEqual', 'assertAlmostEquals', 'assertDictEqual', 'assertEqual', 'assertEquals', 'assertFalse',
           'assertGreater', 'assertGreaterEqual', 'assertIn', 'assertIs', 'assertIsInstance', 'assertIsNone',
           'assertIsNot', 'assertIsNotNone', 'assertItemsEqual', 'assertLess', 'assertLessEqual',
           'assertMultiLineEqual', 'assertNotAlmostEqual', 'assertNotAlmostEquals', 'assertNotContains',
           'assertNotEqual', 'assertNotEquals', 'assertNotIn', 'assertNotIsInstance', 'assertNotRegexpMatches',
           'assertRaises', 'assertRaisesMessage', 'assertRaisesRegexp', 'assertRegexpMatches',
           'assertSetEqual', 'assertTrue', 'assert_')


class PytestAssertChecker(object):
    name = 'flake8-pytest'
    version = __version__

    def __init__(self, tree, filename='(none)', builtins=None):
        self.tree = tree
        self.filename = (filename == 'stdin' and stdin) or filename

    def run(self):
        # Get lines to ignore
        if self.filename == stdin:
            noqa = _get_noqa_lines(self.filename)
        else:
            with open(self.filename, 'r') as file_to_check:
                noqa = _get_noqa_lines(file_to_check.readlines())

        # Run the actual check
        errors = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in ASSERTS and node.lineno not in noqa:
                errors.append({
                    "message": '{0} {1}: {2}'.format(PYTEST_ERROR_CODE, PYTEST_ERROR_MESSAGE, node.func.attr),
                    "line": node.lineno,
                    "col": node.col_offset
                })

        # Yield the found errors
        for error in errors:
            yield (error.get("line"), error.get("col"), error.get("message"), type(self))


def _get_noqa_lines(code):
    tokens = tokenize.generate_tokens(lambda L=iter(code): next(L))
    return [token[2][0] for token in tokens if token[0] == tokenize.COMMENT and
            (token[1].endswith('noqa') or (isinstance(token[0], str) and token[0].endswith('noqa')))]

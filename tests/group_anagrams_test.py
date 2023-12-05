import unittest
import sys
import os
import typing as t

sys.path.insert(0, os.getcwd())

from group_anagrams import groupAnagrams  # noqa: E402


def idempotent(inp: t.Any) -> str:
    return "".join(sorted(str(inp)))


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            idempotent(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])),
            idempotent([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        )
        self.assertEqual(groupAnagrams([""]), [[""]])
        self.assertEqual(groupAnagrams(["a"]), [["a"]])

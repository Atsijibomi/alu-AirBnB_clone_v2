#!/usr/bin/python3
"""Unittest for console.py"""

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import os
from models import storage


class TestConsole(unittest.TestCase):
    """Tests for console.py"""

    def setUp(self):
        """Sets up test methods"""
        self.console = HBNBCommand()
        self.stdout = StringIO()
        self.storage = storage

    def tearDown(self):
        del self.stdout
        del self.storage

    def test_create_state(self):
        """Tests create State command"""
        with patch('sys.stdout', new=self.stdout):
            self.console.onecmd("create State")
        output = self.stdout.getvalue().strip()
        self.assertTrue(output)
        self.assertTrue(len(output) == 36)

    def test_create_state_with_input(self):
        """Tests create State command with input"""
        with patch('sys.stdout', new=self.stdout):
            self.console.onecmd("create State name=\"California\"")
            output1 = self.stdout.getvalue().strip()
            self.console.onecmd("all State")
            output2 = self.stdout.getvalue().strip()
        self.assertIn(output1, output2)
        self.assertIn('California', output2)
        self.assertIn("[State]", self.stdout.getvalue())

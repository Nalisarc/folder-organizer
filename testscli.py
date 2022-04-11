import pytest
import core
import pathlib
import logging

from click.testing import CliRunner

from cli import run

def test_cli_run():
    runner = CliRunner()
    result = runner.invoke(run, [])

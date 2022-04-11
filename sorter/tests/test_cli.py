import pytest
import core
import pathlib
import logging

from click.testing import CliRunner

from cli import run

def test_cli_run():
    runner = CliRunner()
    result = runner.invoke(run, ["--help"])


def test_can_set_verbosity():
    runner = CliRunner()
    result = runner.invoke(run, ["-v"])
    

def test_can_set_recursive():
    runner = CliRunner()
    result = runner.invoke(run, ["-r"])

def test_can_set_directory(tmp_path):
    runner = CliRunner()
    d = tmp_path 
    result = runner.invoke(run, [f"-d {d}"])

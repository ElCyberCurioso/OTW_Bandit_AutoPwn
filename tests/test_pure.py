"""Unit tests for pure helper functions (no network, no heavy deps)."""
from types import SimpleNamespace

import lib.args_utilities as args_utilities
import lib.data_utilities as data_utilities
import lib.exploitation_chain as ec
import lib.recursive_file_decompressor as decompressor
import lib.utilities as utilities

# --- exploitation_chain._user_num ---------------------------------------

def test_user_num_basic():
    assert ec._user_num("bandit0") == 0
    assert ec._user_num("bandit12") == 12
    assert ec._user_num("bandit33") == 33


# --- data_utilities._flatten_fields -------------------------------------

def test_flatten_fields_none():
    assert data_utilities._flatten_fields(None) == []


def test_flatten_fields_flat_list_unchanged():
    assert data_utilities._flatten_fields(["user", "password"]) == ["user", "password"]


def test_flatten_fields_with_sublists():
    assert data_utilities._flatten_fields([["user", "password"], "notes"]) == [
        "user", "password", "notes",
    ]


# --- args_utilities.get_selected_fields ---------------------------------

_ALL = ["user", "password", "details", "tags", "url", "temp_folder", "notes"]


def _args(**flags):
    base = {k: False for k in ("users", "password", "details", "tags", "url",
                               "temp_folder", "notes")}
    base.update(flags)
    return SimpleNamespace(**base)


def test_get_selected_fields_none_selected_returns_all():
    assert args_utilities.get_selected_fields(_args()) == _ALL


def test_get_selected_fields_all_selected_returns_all():
    everything = {k: True for k in ("users", "password", "details", "tags",
                                    "url", "temp_folder", "notes")}
    assert args_utilities.get_selected_fields(_args(**everything)) == _ALL


def test_get_selected_fields_subset():
    assert args_utilities.get_selected_fields(_args(password=True, notes=True)) == [
        "password", "notes",
    ]


# --- recursive_file_decompressor.detect_compression_type ----------------

def test_detect_gzip(tmp_path):
    f = tmp_path / "a.gz"
    f.write_bytes(b"\x1f\x8b\x08\x00rest")
    assert decompressor.detect_compression_type(str(f)) == "gz"


def test_detect_zip(tmp_path):
    f = tmp_path / "a.zip"
    f.write_bytes(b"\x50\x4b\x03\x04rest")
    assert decompressor.detect_compression_type(str(f)) == "zip"


def test_detect_plain_text_is_none(tmp_path):
    f = tmp_path / "a.txt"
    f.write_bytes(b"just plain text, nothing compressed")
    assert decompressor.detect_compression_type(str(f)) is None


# --- utilities.count_elements -------------------------------------------

def test_count_elements_string_is_one():
    assert utilities.count_elements("bandit5") == 1


def test_count_elements_list():
    assert utilities.count_elements(["bandit1", "bandit2", "bandit3"]) == 3


def test_count_elements_non_iterable():
    assert utilities.count_elements(42) == 1


# --- data_utilities.print_boxed -----------------------------------------

def test_print_boxed_frames_text(capsys):
    data_utilities.print_boxed("Hi")
    out = capsys.readouterr().out.splitlines()
    assert out[0] == "+----+"
    assert out[1] == "| Hi |"
    assert out[2] == "+----+"

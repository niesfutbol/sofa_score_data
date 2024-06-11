import sofa_score_data as ssd


def test_obtain_downloaded_files() -> None:
    expected_id: list = [4230530, 4230531, 4230532]
    path: str = "/workdir/tests/data/downloaded_examples/"
    obtained: list = ssd.obtain_downloaded_files(path)
    assert obtained == expected_id


def test_obtain_not_downloaded_files() -> None:
    all_downloaded_files: list = [4230530, 4230531, 4230532]
    all_files: list = ["4230530", 4230531, "4230532", "4230533", 4230534]
    expected: list = [4230533, 4230534]
    obtained: list = ssd.obtain_not_downloaded_files(all_files, all_downloaded_files)
    assert obtained == expected


def test_transfor_dict_of_scalar_to_list() -> None:
    scalar_dictionary: dict = {"a": 1, "b": True, "c": "abc"}
    expected_dictionary: float = {"a": [1], "b": [True], "c": ["abc"]}
    ssd.transfor_dict_of_scalar_to_list(scalar_dictionary)

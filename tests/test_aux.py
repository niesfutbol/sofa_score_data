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
    expected_dictionary: dict = {"a": [1], "b": [True], "c": ["abc"]}
    obtained_dictionary: dict = ssd.transfor_dict_of_scalar_to_list(scalar_dictionary)
    assert obtained_dictionary == expected_dictionary


def test_extract_id_from_filename() -> None:
    filename: str = [
        "match_details_data_4221977.json",
        "match_details_data_4221992.json",
        "match_details_data_4221918.json",
        "match_details_data_4221758.json",
    ]
    expected_id: int = [4221977, 4221992, 4221918, 4221758]
    obtained_id: int = ssd.extract_id_from_filename(filename)
    assert obtained_id == expected_id
    filename_with_error: str = [
        "other_name.csv",
        "match_details_data_4221977.json",
        "match_details_data_4221992.json",
        "match_details_data_4221918.json",
        "match_details_data_4221758.json",
    ]
    expected_id: int = [4221977, 4221992, 4221918, 4221758]
    obtained_id: int = ssd.extract_id_from_filename(filename_with_error)
    assert obtained_id == expected_id

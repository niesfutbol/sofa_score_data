import sofa_score_data as ssd


def test_obtain_downloaded_files() -> None:
    expected_id: list = [4230530, 4230531, 4230532]
    path: str = "/workdir/tests/data/downloaded_examples/"
    obtained: list = ssd.obtain_downloaded_files(path)
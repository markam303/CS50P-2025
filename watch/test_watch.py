import pytest
from watch import parse


def test_notsecure():
    assert (
        parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>')
        == f"https://youtu.be/xvFZjo5PgG0"
    )


def test_notwww():
    assert (
        parse('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>')
        == f"https://youtu.be/xvFZjo5PgG0"
    )


def test_fullurl():
    assert (
        parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>')
        == f"https://youtu.be/xvFZjo5PgG0"
    )


def test_moreattributes():
    assert (
        parse(
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        )
        == f"https://youtu.be/xvFZjo5PgG0"
    )

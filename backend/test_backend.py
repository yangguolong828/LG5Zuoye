import requests


def test_testcase_post():

    r=requests.post(
        'http://127.0.0.1:5000/testcase',
        json={
            'name': "testcase 1",
            'steps': ["step 1", "step 2"]
        }
    )
    assert r.status_code == 200

    r = requests.post(
        'http://127.0.0.1:5000/testcase',
        json={
            'name': "testcase 3",
            'steps': ["step 1", "step 2"]
        }
    )
    assert r.status_code == 200

def test_testcase_delete():
    r=requests.delete(
        'http://127.0.0.1:5000/testcase',
        json={
            'name': "testcase 2"
        }
    )
    assert r.status_code == 200
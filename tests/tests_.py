import pytest

from pmgr.project import Project


@pytest.fixture(scope="function")
def testproj():
    tproj = Project('mytestproj')
    yield tproj
    tproj.delete()

def tests_add(testproj):
    testproj.add_task('dosomething')
    assert 'dosomething' in testproj.get_tasks()

def test_remove(testproj):
    task1 = 'dosomething'
    testproj.add_task(task1)
    testproj.remove_task(task1)
    assert task1 not in testproj.get_tasks() 


def test_show(testproj):
    tasks = []
    tasks.append("hi")
    tasks.append("world")
    tasks.append("bye")

    testproj.add_task("hi")
    testproj.add_task("world")
    testproj.add_task("bye")

    assert tasks == testproj.get_tasks()




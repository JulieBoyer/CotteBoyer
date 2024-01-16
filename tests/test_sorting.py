#test_sorting
#PYTHONPATH=.. python -m pytest .
import sorting_code

def test_bubble():
    assert sorting_code.bubble_sort(["ab","b"])==["ab","b"]
    assert sorting_code.bubble_sort(["ab","AB"])==["AB","ab"]
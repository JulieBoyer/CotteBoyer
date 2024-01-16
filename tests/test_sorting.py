#test_sorting
#PYTHONPATH=.. python -m pytest .
import sorting_code

def test_bubble():
    assert sorting_code.bubble_sort(["ab","b"])==["ab","b"]
    assert sorting_code.bubble_sort(["ab","AB"])==["AB","ab"]
    assert sorting_code.bubble_sort(["ab","AB","cb","cde","CDE"])==["AB","ab","cb","CDE","cde"]
    assert sorting_code.bubble_sort(["agathe","cotte","julie","boyer"])==["agathe","boyer","cotte","julie"]
    assert sorting_code.bubble_sort(["123","321","364","128"])==["123","128","321","364"]
def test_head():
    assert sorting_code.heap_sort(["ab","b"])==["ab","b"]
    assert sorting_code.heap_sort(["ab","AB"])==["AB","ab"]
    assert sorting_code.heap_sort(["ab","AB","cb","cde","CDE"])==["AB","ab","cb","CDE","cde"]
    assert sorting_code.heap_sort(["agathe","cotte","julie","boyer"])==["agathe","boyer","cotte","julie"]
    assert sorting_code.heap_sort(["123","321","364","128"])==["123","128","321","364"]
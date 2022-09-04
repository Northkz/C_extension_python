#include <Python.h>
#include <stdio.h>


long* select_sort(long array[], int N){
    int i, j, min_element;
    for (i = 0; i < N-1; i++) {
        min_element = i;
        for (j = i+1; j < N; j++)
        if (array[j] < array[min_element])
        min_element = j;
        int temp = array[min_element];
        array[min_element] = array[i];
        array[i] = temp;
    }
    return array;
}

static PyObject* selectSort(PyObject* self, PyObject* args) {
    PyObject* list, *final_list;
    long *array;
    
    if (!PyArg_ParseTuple(args, "O", &list))
        return NULL;
    int N = PyObject_Length(list);
    if (N < 0)
        return NULL;
    array = (long *) malloc(sizeof(long) * N);
    for (int index = 0; index < N; index++) {
        PyObject *item;
        item = PyList_GetItem(list, index);
        if (!PyFloat_Check(item))
            array[index] = 0;
        array[index] = PyLong_AsLong(item);
    }
    array = select_sort(array, N);
    final_list = PyList_New(N);
    for (int index = 0; index < N; index++){
        PyObject *item = PyLong_FromLong(array[index]);
        PyList_SetItem(final_list, index, item);
    }
    return final_list;
    
}


static PyMethodDef myMethods[] = {
    { "selectSort", process_list, METH_VARARGS, "Selection sort" },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef myModule = {
    PyModuleDef_HEAD_INIT,
    "myModule",
    "Test Module",
    -1,
    myMethods
};


PyMODINIT_FUNC PyInit_myModule(void)
{
    return PyModule_Create(&myModule);
}

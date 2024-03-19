#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic info about Python
 * lists
 * @p: PyObject pointer to a Python list
 * Description: Python/C API to interact with Python
 * objects in C
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t alloc = ((PyListObject *)p)->allocated;
	Py_ssize_t i;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

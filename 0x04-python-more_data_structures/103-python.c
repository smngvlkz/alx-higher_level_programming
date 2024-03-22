#include <Python.h>

/* Function prototypes */
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints basic info about Python lists
 * @p: pointer to a python object
 */
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
	}
}

/**
 * print_python_bytes - prints basic info about Python bytes objects
 * @p: pointer to a python object
 */
void print_python_bytes(PyObject *p)
{
	unsigned char *str;
	Py_ssize_t size;
	Py_ssize_t i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = (unsigned char *)PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size < 10)
	{
		printf("  first %ld bytes:", size + 1);
	}
	else
	{
		printf("  first 10 bytes:");
		size = 9;
	}
	for (i  = 0; i <= size; i++)
	{
		printf(" %02hhx", str[i]);
	}
	printf("\n");
}

#include <Python.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject pointer to a Python string.
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t len;
	const char *str;
	char *r;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		r = "compact ascii";
	else
		r = "compact unicode object";

	str = PyUnicode_AsUTF8AndSize(p, &len);

	printf(" type: %s\n", r);
	printf(" length: %ld\n", len);
	printf(" value: %s\n", str);
}

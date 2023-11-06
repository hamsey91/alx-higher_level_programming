#include <Python.h>

/**
 * print_python_list_info - Function that prints some basic info
 *			about Python lists.
 *
 * @p: Pointer to the PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int element;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));

	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (element = 0; element < Py_SIZE(p); element++)
		printf("Element %d: %s\n", element, Py_TYPE(PyList_GetItem(p, element))->tp_name);
}

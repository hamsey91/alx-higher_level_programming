#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list_info - Function that prints some basic info
 *			about Python lists.
 *
 * @p: Pointer to the PyObject list.
 */
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int element;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (element = 0; element < size; element++)
	{
		type = (list->ob_item[element])->ob_type->tp_name;
		printf("Element %element: %s\n", element, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[element]);
	}
}

/**
 * print_python_bytes - Function that prints some basic info
 *			about Python bytes.
 *
 * @p: Pointer to the PyObject list.
*/
void print_python_bytes(PyObject *p)
{
	unsigned char i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->op_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->op_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->op_size + 1;
	printf("  first %d bytes: ", size);
	for (i = 0; i < size ; i++)
	{
		printf(" %02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			print(" ");
	}
}

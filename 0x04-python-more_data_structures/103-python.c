#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 * print_python_list - Function that prints some basic info
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
		printf("Element %d: %s\n", element, type);
		if (!strcmp(type, "bytes"))
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
	long int size;
	int element;
	char *try_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &try_str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", try_str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (element = 0; element <= size && element < 10; element++)
		printf(" %02hhx", try_str[element]);
	printf("\n");
}

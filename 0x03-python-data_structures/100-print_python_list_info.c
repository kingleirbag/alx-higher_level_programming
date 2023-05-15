#include <Python.h>

/**
 * print_python_list_info - a C function that prints some
 * basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int pysize, memaloc, count;
	PyObject *obj;

	pysize = Py_SIZE(p);
	memaloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", pysize);
	printf("[*] Allocated = %d\n", memaloc);
	for (count = 0; count < size; count++)
	{
		printf("Element %d: ", count);
		obj = PyList_GetItem(p, count);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}

#include <Python.h>

/**
 * print_python_list_info - a C function that prints some
 * basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int list_size, mem_alloc, count;
	PyObject *py_obj;

	list_size = Py_SIZE(p);
	mem_alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", mem_alloc);

	for (count = 0; count < list_size; count++)
	{
		printf("Element %d: ", count);
		py_obj = PyList_GetItem(p, count);
		printf("%s\n", Py_TYPE(py_obj)->tp_name);
	}
}

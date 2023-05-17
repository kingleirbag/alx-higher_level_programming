#include <Python.h>
/**
 * print_python_list - a C function that prints some
 * basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int py_size, mem_alloc, count;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	py_size = var->ob_size;
	mem_alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", py_size);
	printf("[*] Allocated = %d\n",mem_ alloc);

	for (count = 0; count < py_size; count++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", count, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
/**
 * print_python_bytes - get info about Python byte objects.
 * @p: A PyObject byte
 */
void print_python_bytes(PyObject *p)
{
	unsigned char count, py_size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		py_size = 10;
	else
		py_size = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %d bytes: ", py_size);
	for (count = 0; count < py_size; counte++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (count == (py_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

#include <python.h>
#include <iostream>
#include <windows.h>
// function section

static PyObject* getx(PyObject* self, PyObject* args)
{
	CONSOLE_SCREEN_BUFFER_INFO csbi;
	if (!GetConsoleScreenBufferInfo(
		GetStdHandle(STD_OUTPUT_HANDLE),
		&csbi
	))
		return Py_BuildValue("s", "error!");

	return Py_BuildValue("i", csbi.dwCursorPosition.X);
}

static PyObject* gety(PyObject* self, PyObject* args)
{
	CONSOLE_SCREEN_BUFFER_INFO csbi;
	if (!GetConsoleScreenBufferInfo(
		GetStdHandle(STD_OUTPUT_HANDLE),
		&csbi
	))
		return Py_BuildValue("s", "error!");
	return Py_BuildValue("i", csbi.dwCursorPosition.Y);
}

//module definition struct
static PyMethodDef devdeltaMethods[] = {
	{"getx", getx, METH_VARARGS, "get x coordinate of window."},
	{"gety", gety, METH_VARARGS, "get y coordinate of window."},
	{NULL, NULL, 0, NULL}
};

//module methods definition struct
static struct PyModuleDef devdeltamodule = {
	PyModuleDef_HEAD_INIT,
	"devdelta",
	"DevDelta development library.",
	-1,
	devdeltaMethods
};

// initialization of module.
PyMODINIT_FUNC PyInit_devdelta(void)
{
	return PyModule_Create(&devdeltamodule);
}

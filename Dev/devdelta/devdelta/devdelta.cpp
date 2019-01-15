#include <python.h>
#include <iostream>
#include <windows.h>

static PyObject* devdelta(PyObject* self, PyObject* args)
{
	/* initialize random seed: */
	int random = rand() % 10;
	Py_INCREF(Py_None);
	std::cout << random << " random number";
	return Py_None;
}
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
static PyMethodDef DevdeltaMethods[] = {
	{"devdelta", devdelta, METH_VARARGS, "generate random number."}, 
	{"getx", getx, METH_VARARGS, "get x coordinate of window."},
	{"gety", gety, METH_VARARGS, "get y coordinate of window."},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef devdeltamodule = {
	PyModuleDef_HEAD_INIT,
	"devdelta",
	NULL,
	-1,
	DevdeltaMethods 
};

static struct PyModuleDef getxmodule = {
	PyModuleDef_HEAD_INIT,
	"getx",
	NULL,
	-1,
	DevdeltaMethods
};

static struct PyModuleDef getymodule = {
	PyModuleDef_HEAD_INIT,
	"gety",
	NULL,
	-1,
	DevdeltaMethods
};
PyMODINIT_FUNC PyInit_devdelta(void)
{
	return PyModule_Create(&devdeltamodule);
}
PyMODINIT_FUNC PyInit_getx(void)
{
	return PyModule_Create(&getxmodule);
}
PyMODINIT_FUNC PyInit_gety(void)
{
	return PyModule_Create(&getymodule);
}
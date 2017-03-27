from ipykernel.kernelapp import IPKernelApp
from . import ElmKernel

IPKernelApp.launch_instance(kernel_class=ElmKernel)

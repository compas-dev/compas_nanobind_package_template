from {{cookiecutter.project_slug}}._vectors_reference import DoubleVector
from {{cookiecutter.project_slug}}._vectors_reference import subtract_inplace

a = DoubleVector([1, 2, 3])
b = DoubleVector([4, 6, 8])

subtract_inplace(a, b)

for i in range(len(a)):
    print(a[i])

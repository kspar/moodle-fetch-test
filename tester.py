from grader import *
from rattad import *
from random import randint

FUNCTION_NAME = 'vahimatest_suurim'

def solution(mat):
    return max([min(row) for row in mat])

def random_matrix():
    rows = randint(1, 10)
    cols = randint(1, 5)
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(randint(-10, 10))
        result.append(row)
    return result



def gen_test(test_arg,desc):

    @test
    @expose_ast
    @set_description(desc)
    def do_test(m, AST):
        must_not_have_input(AST)

        must_have_func_def_toplevel(m.module, FUNCTION_NAME)
        actual_func_node = get_function_def_node(AST, FUNCTION_NAME)
        must_have_n_params(actual_func_node, 1)

        actual_func_obj = get_function(m.module, FUNCTION_NAME)
        must_have_equal_return_values(solution, actual_func_obj, FUNCTION_NAME, test_arg, args_repr=matrix_repr(test_arg))



a = [[1, 2],
     [1, 0]]
gen_test(a, 'Lihtne maatriks 1')

b = [[-1, 9],
     [5, -1],
     [-1, 1]]
gen_test(b, 'Lihtne maatriks 2')

c = [[1, 9],
     [5, 1],
     [2, 2],
     [3, 6]]
gen_test(c, 'Keerulisem maatriks 1')

d = [[1, 0, -9001]]
gen_test(d, 'Keerulisem maatriks 2')

e = [[42]]
gen_test(e, 'Üheelemendiline maatriks')

for i in range(10):
    gen_test(random_matrix(),'Juhuslik maatriks {}'.format(i))



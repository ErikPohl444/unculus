from unculus_node import unculus_node


def foo(z_func_arg):
    print(f"doing something with value {str(z_func_arg)}")
    print(f"adding zappo to z and making a string {str(z_func_arg + zappo)}")


def bar(z_func_arg):
    print(f'doing something with entrance token {str(z_func_arg)}')
    print(f"adding zappo to z and making a string {str(z_func_arg + zappo)}")


zappo = 2
one = unculus_node('one', 1, foo, bar)
two = unculus_node('two', 2, foo, bar)

one.add_turnstile(1, None)
one.add_turnstile(2, two)
two.add_turnstile(3, one)
two.add_turnstile(4, two)

head = one
z = [2, 3, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 1]
try:
    head.consume_and_print(z)
except:
    pass
try:
    print(head.is_consumed_completing_sequence(z))
except:
    pass

z = [2, 3, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3]
print(head.is_consumed_completing_sequence(z))

z = [1]
print(head.is_consumed_completing_sequence(z))

z = [2, 3, 1, 2]
print(head.is_consumed_completing_sequence(z))

z = [7, 3, 1, 2]
print(head.is_consumed_completing_sequence(z))

print("single evaluation test here -------------------------")
nextone = head.evaluate_token(2)
print(f"moved to {nextone.value}")

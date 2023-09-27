def function(t, y):
    return t * y + 1


# ======initial value of t & y are given=============
t = [0]
y = [1]
# ===================================================

upperLimit = 1  # upper limit of t
h = .25  # step size
i = 0
while t[i] < upperLimit:  # if i use equal sign then t will exceed the upper limit by .25
    """the euler method(forward) is applied here"""
    t.append(t[i] + h)
    y.append(y[i] + h * function(t[i], y[i]))
    i += 1

# ========printing the result in a table===============
print("iteration", "  ti  ", "  yi  ")
for j in range(i):
    print("-------------------------")
    print("{:^9}|{:^6.2f}| {:^6.4f}".format(j, t[j], y[j]))
# =====================================================

# the final result.......
print("\nso the approximate solution of given ODE is {:6.4f}".format(y[j]))
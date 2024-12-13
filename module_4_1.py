from fake_math import fake_div as divide_fake
from true_math import true_div as divide_true

def main():

    result1 = divide_fake(69, 3)
    result2 = divide_fake(3, 0)
    result3 = divide_true(49, 7)
    result4 = divide_true(15, 0)


    print(result1)
    print(result2)
    print(result3)
    print(result4)

if __name__ == "__main__":
    main()



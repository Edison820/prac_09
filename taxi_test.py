"""
CP1404/CP5632 Practical
Taxi-test

"""
import prac_09.trees as trees


def main():
    tree_list = [trees.Tree(), trees.EvenTree(), trees.UpsideDownTree(),
                 trees.WideTree(), trees.QuickTree(), trees.FruitTree(),
                 trees.PineTree()]


    for tree in tree_list:
        print(tree.__class__)
        print(tree)

    print("Time to grow!")
    for _ in range(5):
        for tree in tree_list:
            tree.grow(5, 2)

    for tree in tree_list:
        print(tree.__class__)
        print(tree)


main()
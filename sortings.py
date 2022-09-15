from datetime import datetime
from random import randint


def get_array(length: int):
    array = []
    for i in range(length):
        array.append(randint(1, length))
    print(f'{array=}')
    return array


def bubble_sorting(args):
    global end_time
    start_time = datetime.now()
    count = True
    for i in range(len(args) - 1):

        if count == False:
            break
        count = False
        for j in range(len(args) - i - 1):

            # print(i, j, count, args)
            if args[j] > args[j + 1]:
                args[j], args[j + 1] = args[j + 1], args[j]
                count = True
    end_time = datetime.now() - start_time
    print('Bubble ascended sorting was finished')
    return args


def bubble_sorting_desc(args):
    global end_time
    start_time = datetime.now()
    count = True
    for i in range(len(args) - 1):
        if count == False:
            break
        count = False
        for j in range(len(args) - i - 1):
            if args[j] < args[j + 1]:
                args[j], args[j + 1] = args[j + 1], args[j]
                count = True
    end_time = datetime.now() - start_time
    print('Bubble descend sorting was finished')
    return args


def insert_sorting(args):
    for i in range(1, len(args)):
        while i > 0 and args[i - 1] > args[i]:
            args[i - 1], args[i] = args[i], args[i - 1]
            i -= 1
    print('Insert ascended sorting was finished')
    return args


def insert_sorting_desc(args):
    for i in range(1, len(args)):
        while i < 0 and args[i - 1] > args[i]:
            args[i - 1], args[i] = args[i], args[i - 1]
            i -= 1
    print('Insert descend sorting was finished')
    return args


def choice_sorting(args):
    for i in range(len(args) - 1):
        for j in range(i + 1, len(args)):
            if args[j] < args[i]:
                args[j], args[i] = args[i], args[j]
    print('Choice ascended sorting was finished')
    return args


def choice_sorting_desc(args):
    for i in range(len(args) - 1):
        for j in range(i + 1, len(args)):
            if args[j] > args[i]:
                args[j], args[i] = args[i], args[j]
    print('Choice descend sorting was finished')
    return args


def merge_sorting():
    def merge_sorting_(args):
        n = len(args)
        if n <= 1:
            return args
        mid = n // 2
        left_sort_list = merge_sorting_(args[:mid])
        right_sort_list = merge_sorting_(args[mid:])
        left_pointer = 0
        right_pointer = 0
        sorted_list = []
        while left_pointer < len(left_sort_list) and right_pointer < len(right_sort_list):
            if left_sort_list[left_pointer] < right_sort_list[right_pointer]:
                sorted_list.append(left_sort_list[left_pointer])
                left_pointer += 1
            else:
                sorted_list.append(right_sort_list[right_pointer])
                right_pointer += 1
        sorted_list += left_sort_list[left_pointer:]
        sorted_list += right_sort_list[right_pointer:]
        return sorted_list

    print('Merge ascended sorting was finished')
    return merge_sorting_


def merge_sorting_desc():
    def merge_sorting_desc_(args):
        n = len(args)
        if n <= 1:
            return args
        mid = n // 2
        left_sort_list = merge_sorting_desc_(args[:mid])
        right_sort_list = merge_sorting_desc_(args[mid:])
        left_pointer = 0
        right_pointer = 0
        sorted_list = []
        while left_pointer < len(left_sort_list) and right_pointer < len(right_sort_list):
            if left_sort_list[left_pointer] > right_sort_list[right_pointer]:
                sorted_list.append(left_sort_list[left_pointer])
                left_pointer += 1
            else:
                sorted_list.append(right_sort_list[right_pointer])
                right_pointer += 1
        sorted_list += left_sort_list[left_pointer:]
        sorted_list += right_sort_list[right_pointer:]
        return sorted_list

    print('Merge descended sorting was finished')
    return merge_sorting_desc_


def quick_sorting():
    def quick_sorting_(args):
        global sorted_list
        if len(args) > 1:
            pointer = randint(0, len(args) - 1)
            low = [i for i in args if i < args[pointer]]
            height = [i for i in args if i > args[pointer]]
            equal = [i for i in args if i == args[pointer]]
            args = quick_sorting_(low) + equal + quick_sorting_(height)
        return args

    print('Quick ascended sorting was finished')
    return quick_sorting_


def quick_sorting_desc():
    def quick_sorting_desc_(args):
        global sorted_list
        if len(args) > 1:
            pointer = randint(0, len(args) - 1)
            low = [i for i in args if i < args[pointer]]
            height = [i for i in args if i > args[pointer]]
            equal = [i for i in args if i == args[pointer]]
            args = quick_sorting_desc_(height) + equal + quick_sorting_desc_(low)
        return args

    print('Quick descended sorting was finished')
    return quick_sorting_desc_



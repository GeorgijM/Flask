from flask import Flask, render_template, request
import timeit
import sortings
import copy

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def index():
    global form1, sorted_array_asc, random_array, time_bubble_asc
    array_for_desc_sorting = []
    array_for_asc_sorting = []
    sorted_array_asc = []
    sorted_array_desc = []
    random_array = []

    if request.method == 'POST':
        form1 = request.form.get('array_lengs')
        if form1 == '':
            form1 = 0
        form_sorting_type = request.form.get('choice')
        random_array = sortings.get_array(int(form1))  # needed fork for usage in asc and desk sortings
        array_for_asc_sorting = copy.deepcopy(random_array)
        array_for_desc_sorting = copy.deepcopy(random_array)
        if form_sorting_type == 'Bubble':
            sorted_array_asc = sortings.bubble_sorting(array_for_asc_sorting)
            sorted_array_desc = sortings.bubble_sorting_desc(array_for_desc_sorting)
        if form_sorting_type == 'Choice':
            sorted_array_asc = sortings.choice_sorting(array_for_asc_sorting)
            sorted_array_desc = sortings.choice_sorting_desc(array_for_desc_sorting)
        if form_sorting_type == 'Insert':
            sorted_array_asc = sortings.insert_sorting(array_for_asc_sorting)
            sorted_array_desc = sortings.insert_sorting_desc(array_for_desc_sorting)
        if form_sorting_type == 'Merge':
            sorted_array_asc = sortings.merge_sorting()(array_for_asc_sorting)
            sorted_array_desc = sortings.merge_sorting_desc()(array_for_desc_sorting)
        if form_sorting_type == 'Quick':
            sorted_array_asc = sortings.quick_sorting()(array_for_asc_sorting)
            sorted_array_desc = sortings.quick_sorting_desc()(array_for_desc_sorting)
        else:
            sorted_array_asc = sorted(array_for_asc_sorting)
            sorted_array_desc = sorted_array_asc[::-1]

    time_bubble_asc = timeit.timeit(lambda: sortings.bubble_sorting(array_for_asc_sorting), number=2) / 2
    time_bubble_desc = timeit.timeit(lambda: sortings.bubble_sorting_desc(array_for_desc_sorting), number=2) / 2

    time_choice_asc = timeit.timeit(lambda: sortings.choice_sorting(array_for_asc_sorting), number=2) / 2
    time_choice_desc = timeit.timeit(lambda: sortings.choice_sorting_desc(array_for_desc_sorting), number=2) / 2

    time_insert_asc = timeit.timeit(lambda: sortings.insert_sorting(array_for_asc_sorting), number=2) / 2
    time_insert_desc = timeit.timeit(lambda: sortings.insert_sorting_desc(array_for_desc_sorting), number=2) / 2


    time_merge_asc = timeit.timeit(lambda: sortings.merge_sorting()(array_for_asc_sorting), number=2) / 2
    time_merge_desc = timeit.timeit(lambda: sortings.merge_sorting_desc()(array_for_desc_sorting), number=2) / 2

    time_quick_asc = timeit.timeit(lambda: sortings.quick_sorting()(array_for_asc_sorting), number=2) / 2
    time_quick_desc = timeit.timeit(lambda: sortings.quick_sorting_desc()(array_for_desc_sorting), number=2) / 2

    template_context = dict(random_array=random_array,
                            sorted_array_asc=sorted_array_asc, sorted_array_desc=sorted_array_desc,
                            time_bubble_asc=time_bubble_asc, time_bubble_desc=time_bubble_desc,
                            time_choice_asc=time_choice_asc, time_choice_desc=time_choice_desc,
                            time_insert_asc=time_insert_asc, time_insert_desc=time_insert_desc,
                            time_merge_asc=time_merge_asc, time_merge_desc=time_merge_desc,
                            time_quick_asc=time_quick_asc,  time_quick_desc= time_quick_desc)
    return render_template('index2.html', **template_context)

if __name__ == "__main__":
    app.run(debug=True)

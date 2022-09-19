from flask import Flask, render_template, request, redirect, url_for
import timeit
import sortings
import copy
import sqlite3
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WkdfjdkWJK;d#lkdfsj@11221kjksdfjllkjdi'


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
        if form1 is None:
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

        # name = request.form.get('name')
        # comment = request.form.get('comment')
        # print(f'{name}')
        # print((f'{comment}'))



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

    # Code for the blog
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    comments = conn.execute('SELECT * FROM comments').fetchall()

    print(posts[1][2])
    print(comments[0]['name'])
    print(comments[0]['comment'])
    print(comments[0]['id'])

    conn.close()

    template_context = dict(random_array=random_array,
                            sorted_array_asc=sorted_array_asc, sorted_array_desc=sorted_array_desc,
                            time_bubble_asc=time_bubble_asc, time_bubble_desc=time_bubble_desc,
                            time_choice_asc=time_choice_asc, time_choice_desc=time_choice_desc,
                            time_insert_asc=time_insert_asc, time_insert_desc=time_insert_desc,
                            time_merge_asc=time_merge_asc, time_merge_desc=time_merge_desc,
                            time_quick_asc=time_quick_asc, time_quick_desc=time_quick_desc,
                            posts=posts, comments=comments)
    # comment_tittle = comment_tittle, comment_content = comment_content
    return render_template('index2.html', **template_context)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

# Part of code for database usage
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/create_comment', methods=('GET', 'POST'))
def create_comment():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']



        conn = get_db_connection()
        conn.execute('INSERT INTO comments (name, comment) VALUES (?, ?)',
                     (name, comment))
        conn.commit()
        conn.close()

    return redirect(url_for('index'))


@app.route('/<int:id>/delete', methods=('POST',))
def delete_comment(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM comments WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)

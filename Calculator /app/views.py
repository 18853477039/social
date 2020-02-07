from flask import Blueprint, render_template, request

bp = Blueprint('blue', __name__)


@bp.route('/')
def hello_world():
    return 'Hello World!'


@bp.route('/cla/', methods=['GET', 'POST'])
def cla():
    print("??")
    if request.method == 'POST':
        print(1)
        # fir_num = request.form.get('fir_num')
        # sec_num = request.form.get('sec_num')

    return render_template('calculator.html')


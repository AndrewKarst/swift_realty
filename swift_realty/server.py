from flask import Flask, request, render_template

application = Flask(__name__)


@application.route('/amortization-calculator', methods=['GET', 'POST'])
def amortization_calculator():
    form = AmortizationForm()
    amount = schedule = None
    if request.method == 'POST' and form.validate_on_submit():
        amount = calculate_amortization_amount(form.principal.data, form.interest_rate.data / 100 / form.frequency.data,
                                               form.period.data * form.frequency.data)
        schedule = list(amortization_schedule(form.principal.data, form.interest_rate.data / 100 / form.frequency.data,
                                              form.period.data * form.frequency.data))
    return render_template('resources.html', form=form, amortization_amount=amount, amortization_schedule=schedule)

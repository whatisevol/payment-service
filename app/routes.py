# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import NameForm
from hashlib import sha256
import json
import requests
from app.models import Payment
from app import db


@app.route('/', methods=['GET', 'POST'])
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = NameForm()
    if form.validate_on_submit():
        # db.create_all()
        try:
            payment = Payment(amount=form.amount.data,
                              currency=form.currency.data,
                              description=form.description.data)
            db.session.add(payment)
            db.session.commit()
            db.session.refresh(payment)
        except Exception as message:
            app.logger.error(message)
        shop_order_id = payment.id
        data = dict()
        currency_value = app.config['CURRENCYS'][payment.currency]
        if payment.currency == 'EUR':
            data['amount'] = str(payment.amount)
            data['currency'] = str(currency_value)
            data['shop_id'] = str(app.config['SHOP_ID'])
            data['shop_order_id'] = str(shop_order_id)
            data['sign'] = create_sign(app.config['EUR_REQUIRED'], data)
            data['description'] = payment.description
            app.logger.info(f'EUR payment data: {data}')
            return render_template('payment.html', title='eur payment', data=data, url=app.config['URL_EUR'])

        elif payment.currency == 'USD':
            headers = {'Content-Type': 'application/json'}
            data['payer_currency'] = str(currency_value)
            data['shop_amount'] = str(payment.amount)
            data['shop_currency'] = str(currency_value)
            data['shop_id'] = str(app.config['SHOP_ID'])
            data['shop_order_id'] = str(shop_order_id)
            data['sign'] = create_sign(app.config['USD_REQUIRED'], data)
            app.logger.info(f'USD payment data: {data}')
            try:
                server_return = requests.post(
                    url=app.config['URL_USD'],
                    headers=headers,
                    data=json.dumps(data)
                ).json()
                if server_return['data']:
                    app.logger.info(f"USD payment, server respond data: {server_return['data']}")
                    return redirect(server_return['data']['url'])
                else:
                    app.logger.error(server_return['message'])
            except Exception as message:
                app.logger.error(message)

        elif payment.currency == 'RUB':
            headers = {'Content-Type': 'application/json'}
            data['amount'] = str(payment.amount)
            data['currency'] = str(currency_value)
            data['payway'] = app.config['PAYWAY']
            data['shop_id'] = str(app.config['SHOP_ID'])
            data['shop_order_id'] = str(shop_order_id)
            data['sign'] = create_sign(app.config['RUB_REQUIRED'], data)
            app.logger.info(f'RUB payment data: {data}')
            try:
                server_return = requests.post(
                    url=app.config['URL_RUB'],
                    data=json.dumps(data),
                    headers=headers).json()
                if server_return['data']:
                    app.logger.info(f"RUB payment, server respond data: {server_return['data']}")
                    return render_template("payment.html", data=server_return['data']['data'],
                                           url=server_return['data']['url'])
                else:
                    app.logger.error(server_return['message'])
            except Exception as message:
                app.logger.error(message)
    return render_template('form.html', title='form', form=form)


def create_sign(required, data):
    sign = ':'.join([data.get(item) for item in sorted(required)]) + app.config['SECRET_KEY']
    return sha256(sign.encode()).hexdigest()

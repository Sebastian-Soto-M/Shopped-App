import json

import requests
from flask import Blueprint, redirect, render_template, request, url_for


r_bundle = Blueprint('r_bundle', __name__,
                     static_folder='static')


@r_bundle.route('/bundle/home')
def home():
    return redirect(url_for('base_r.home'))

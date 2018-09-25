# -*- coding: utf-8 -*-
"""
    chimp

    Implements the view function for subscription

"""
from nereid import request, jsonify, current_app, current_website

from mailchimp3 import MailChimp
from mailchimp3.mailchimpclient import MailChimpError


def list_subscribe():
    """Subscribes an user to the mailing list

    Inspected arguments in a POST request

    If first_name and last_name is given it is used
    Else name is split into two to be used

    Then the form is inspected for `mailing_list`. If provided the value
    is used as ID for the subscription. If not the default list is used for
    subscription. you could put in this value as a hidden field in the form

    Always returns a JSON response:
    {
        'success': True or False,
        'message': A message (Not recommended to be displayed to user)
    }
    """
    if not current_website.mailchimp_api_key:
        current_app.logger.error("nereid-mailchimp No API key")
        return jsonify(
            success=False,
            message="No API Configured"
        )

    if request.method == 'POST':
        # Mailchimp requires first name and last name, but nereid probably
        # took only the name field. Check for the keys to decide what to pick
        email = request.values['email']

        merge_vars = {}
        keys = request.values.keys()

        if 'first_name' in keys and 'last_name' in keys:
            merge_vars['FNAME'], merge_vars['LNAME'] = (
                request.values['first_name'], request.values['last_name'])
        elif 'name' in keys:
            try:
                merge_vars['FNAME'], merge_vars['LNAME'] = request.values[
                    'name'].split(' ', 1)
            except ValueError:
                merge_vars['FNAME'] = merge_vars['LNAME'] = \
                    request.values['name']
        else:
            merge_vars.update({'FIRST': '', 'LAST': ''})

        mailchimp_client = MailChimp(
            request.nereid_website.mailchimp_api_key
        )

        mailing_list = request.values['mailing_list'] \
            if 'mailing_list' in keys else None
        if mailing_list is None:
            # If no mailing list was there in the form then use the default one
            mailing_list_name = current_website.mailchimp_default_list
            lists = mailchimp_client.lists.all()
            mailing_list_name = request.nereid_website.mailchimp_default_list
            for each_list in lists['lists']:
                if each_list['name'] == mailing_list_name:
                    mailing_list = each_list['id']
                    break
            else:
                return jsonify(
                    success=False,
                    message="No mailing list specified, default one not found"
                )
        #  Call Subscribe
        merge_vars['OPTIN_IP'] = request.remote_addr
        try:
            mailchimp_client.lists.members.create(mailing_list, {
                'email_address': email,
                'status': 'subscribed',
                'merge_fields': merge_vars,
            })
        except MailChimpError, exc:
            return jsonify(success=False, message=exc[0])
        return jsonify(success=True, message="Successfuly subscribed user!")

# -*- coding: utf8 -*-
import hmac
import hashlib
import urlparse

import requests


class DDNSClient(object):
    sig_flag = 'sha256'
    api_prefix = '/api/v1'

    def __init__(self, endpoint, sig_key, sig_value):

        if not endpoint.endwith('/'):
            endpoint += '/'
        
        self.endpoint = endpoint
        self.sig_key = sig_key
        self.sig_value = sig_value

    def gen_signature(self, **kwargs):
        keys = kwargs.keys()
        keys.sort()
        sig_list = []
        for k in keys:
            sig_list.append('{}={}'.format(k, kwargs[k]))
        sig_ogn = '&'.join(sig_list)
        if self.sig_flag == 'sha256':
            signature = hmac.new(self.sig_value, sig_ogn, hashlib.sha256).hexdigest()
        elif self.sig_flag == 'sha1':
            signature = hmac.new(self.sig_value, signature, hashlib.sha1).hexdigest()
        return signature

    def version(self):
        res = requests.get(urlparse.urljoin(self.endpoint, self.api_prefix + '/version'))
        if res.status_code == 200:
            return res.json()
        else:
            return {'meta': {'code': res.status_code}}
    
    def ip(self):
        res = requests.get(urlparse.urljoin(self.endpoint, self.api_prefix + '/ip'))
        if res.status_code == 200:
            return res.json()
        else:
            return {'meta': {'code': res.status_code}}
    
    def create_resource(self, mac_id, ip_address, domain_url):
        res = requests.post(
            urlparse.urljoin(
                self.endpoint, self.api_prefix + '/create_resource'
            ),
            json={
                'mac_id': mac_id,
                'ip_address': ip_address,
                'domain_url': domain_url,
                'signature': self.gen_signature(mac_id=mac_id, ip_address=ip_address, domain_url=domain_url),
                'sig_key': self.sig_key
            }
        )
        if res.status_code == 200:
            return res.json()
        else:
            return {'meta': {'code': res.status_code}}

    def update_ip(self, mac_id, ip_address, domain_url):
        res = requests.post(
            urlparse.urljoin(
                self.endpoint, self.api_prefix + '/update_ip'
            ),
            json={
                'mac_id': mac_id,
                'ip_address': ip_address,
                'domain_url': domain_url,
                'signature': self.gen_signature(mac_id=mac_id, ip_address=ip_address, domain_url=domain_url),
                'sig_key': self.sig_key
            }
        )

        if res.status_code == 200:
            return res.json()
        else:
            return {'meta': {'code': res.status_code}}

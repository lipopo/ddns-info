from unittest import TestCase, main
from ddns_client import DDNSClient

class TestDDNSClient(TestCase):

    def setUp(self):
        self._client = DDNSClient(
            'https://1068773955327057.cn-beijing.fc.aliyuncs.com/2016-08-15/proxy/ddns/ddns',
            '430', 'Yzk1MjUxNzdhMDQ0NDQ5YzgyZTBlZDgwODY0NDc1MjI'
        )

    def test_ip(self):
        ip_res = self._client.ip()
        self.assertEqual(
            ip_res.get('meta', {}).get('code'), 200
        )
    
    def test_version(self):
        version_res = self._client.version()
        self.assertEqual(
            version_res.get('meta', {}).get('code'), 200
        )
        self.assertEqual(
            version_res.get('version'), 'api_v1'
        )

if __name__ == '__main__':
    main()

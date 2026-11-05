import importlib.util
import unittest


class PortalTests(unittest.TestCase):
    def test_api_info_returns_identity(self):
        self.assertIsNotNone(importlib.util.find_spec('app'), 'Aplikasi Flask belum dibuat')
        from app import app
        response = app.test_client().get('/api/info')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['layanan'], 'Portal PMB Universitas Teknologi Muhammadiyah')
        self.assertEqual(data['versi'], 'v1')
        self.assertEqual(data['nama'], 'Andi Syafira')
        self.assertEqual(data['nim'], '24024600037')
        for key in ['gelombang', 'lingkungan', 'region', 'commit', 'id_instance', 'permintaan_ke', 'waktu_utc']:
            self.assertIn(key, data)

    def test_homepage_identity_and_links(self):
        from app import app
        response = app.test_client().get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'text/html')
        html = response.get_data(as_text=True)
        self.assertIn('Flask App with CI/CD Test, NIM: 24024600037', html)
        self.assertIn('Andi Syafira', html)
        for target in ['/health', '/api/info']:
            self.assertIn(f'href="{target}"', html)
            self.assertEqual(app.test_client().get(target).status_code, 200)

    def test_no_foreign_identity_leaks(self):
        from app import app
        html = app.test_client().get('/').get_data(as_text=True)
        payload = app.test_client().get('/api/info').get_data(as_text=True)
        for foreign in ['2402600016', 'Gilang', 'glnggggzr']:
            self.assertNotIn(foreign, html)
            self.assertNotIn(foreign, payload)

    def test_health_is_ok(self):
        from app import app
        response = app.test_client().get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'status': 'ok'})


if __name__ == '__main__':
    unittest.main()

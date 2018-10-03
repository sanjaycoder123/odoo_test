{
    'name': 'Shop Test',
    'version': '1.0',
    'category': 'Service',
    'sequence': 10,
    'summary': 'Services application fpr sesting perpous',
    'description': """
            This Module allows you create and product order
            """,
    'author': 'Saasmate',
    'website': 'https://www.saasmate.com.au',
    'depends': ['base', 'sale','stock'],
    'data': [
            'sale_test_view.xml',
            ],

    'css': [],
    'installable': True,
    'auto_install': True,
    'application': True,
}
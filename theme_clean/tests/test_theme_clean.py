# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import TransactionCase, tagged


@tagged('post_install', '-at_install')
class TestThemeClean(TransactionCase):
    """Test cases for theme_clean module"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.theme_utils = cls.env['theme.utils']
        cls.ir_module_module = cls.env['ir.module.module']
        cls.ir_ui_view = cls.env['ir.ui.view']
        
        # Get the theme_clean module
        cls.theme_clean_module = cls.ir_module_module.search([
            ('name', '=', 'theme_clean')
        ], limit=1)
        
        # Ensure website module is installed (required for theme.utils)
        cls.website_module = cls.ir_module_module.search([
            ('name', '=', 'website')
        ], limit=1)
        if cls.website_module.state != 'installed':
            cls.website_module.button_immediate_install()

    def test_01_theme_clean_model_exists(self):
        """Test that ThemeClean model exists and inherits from theme.utils"""
        self.assertTrue(
            self.env['theme.utils']._name == 'theme.utils',
            "theme.utils model should exist"
        )
        
        # Check that theme_clean module provides ThemeClean model
        theme_clean_model = self.env['theme.utils']
        self.assertTrue(
            hasattr(theme_clean_model, '_theme_clean_post_copy'),
            "ThemeClean model should have _theme_clean_post_copy method"
        )

    def test_02_theme_clean_post_copy_method_exists(self):
        """Test that _theme_clean_post_copy method exists and is callable"""
        theme_utils = self.env['theme.utils']
        
        # Check method exists
        self.assertTrue(
            hasattr(theme_utils, '_theme_clean_post_copy'),
            "_theme_clean_post_copy method should exist"
        )
        
        # Check it's callable
        self.assertTrue(
            callable(getattr(theme_utils, '_theme_clean_post_copy', None)),
            "_theme_clean_post_copy should be callable"
        )

    def test_03_theme_clean_post_copy_enables_header_view(self):
        """Test that _theme_clean_post_copy enables website.template_header_default view"""
        theme_utils = self.env['theme.utils']
        
        # Disable the view first to ensure we can test enabling it
        theme_utils.disable_view('website.template_header_default')
        
        # Verify view is disabled
        header_view = self.ir_ui_view.search([
            ('key', '=', 'website.template_header_default')
        ], limit=1)
        if header_view:
            self.assertFalse(
                header_view.active,
                "Header view should be disabled before test"
            )
        
        # Call the method
        if self.theme_clean_module:
            theme_utils._theme_clean_post_copy(self.theme_clean_module)
        
        # Verify view is enabled
        header_view = self.ir_ui_view.search([
            ('key', '=', 'website.template_header_default')
        ], limit=1)
        if header_view:
            self.assertTrue(
                header_view.active,
                "Header view should be enabled after _theme_clean_post_copy"
            )

    def test_04_theme_clean_post_copy_enables_footer_view(self):
        """Test that _theme_clean_post_copy enables website.template_footer_contact view"""
        theme_utils = self.env['theme.utils']
        
        # Disable the view first to ensure we can test enabling it
        theme_utils.disable_view('website.template_footer_contact')
        
        # Verify view is disabled
        footer_view = self.ir_ui_view.search([
            ('key', '=', 'website.template_footer_contact')
        ], limit=1)
        if footer_view:
            self.assertFalse(
                footer_view.active,
                "Footer view should be disabled before test"
            )
        
        # Call the method
        if self.theme_clean_module:
            theme_utils._theme_clean_post_copy(self.theme_clean_module)
        
        # Verify view is enabled
        footer_view = self.ir_ui_view.search([
            ('key', '=', 'website.template_footer_contact')
        ], limit=1)
        if footer_view:
            self.assertTrue(
                footer_view.active,
                "Footer view should be enabled after _theme_clean_post_copy"
            )

    def test_05_theme_clean_post_copy_enables_both_views(self):
        """Test that _theme_clean_post_copy enables both header and footer views"""
        theme_utils = self.env['theme.utils']
        
        # Disable both views first
        theme_utils.disable_view('website.template_header_default')
        theme_utils.disable_view('website.template_footer_contact')
        
        # Call the method
        if self.theme_clean_module:
            theme_utils._theme_clean_post_copy(self.theme_clean_module)
        
        # Verify both views are enabled
        header_view = self.ir_ui_view.search([
            ('key', '=', 'website.template_header_default')
        ], limit=1)
        footer_view = self.ir_ui_view.search([
            ('key', '=', 'website.template_footer_contact')
        ], limit=1)
        
        if header_view:
            self.assertTrue(
                header_view.active,
                "Header view should be enabled"
            )
        if footer_view:
            self.assertTrue(
                footer_view.active,
                "Footer view should be enabled"
            )

    def test_06_theme_clean_post_copy_with_none_module(self):
        """Test that _theme_clean_post_copy handles None module parameter gracefully"""
        theme_utils = self.env['theme.utils']
        
        # Should not raise an error even with None
        try:
            theme_utils._theme_clean_post_copy(None)
        except Exception as e:
            self.fail(
                f"_theme_clean_post_copy should handle None module gracefully, "
                f"but raised {type(e).__name__}: {e}"
            )

    def test_07_theme_clean_post_copy_idempotent(self):
        """Test that calling _theme_clean_post_copy multiple times is idempotent"""
        theme_utils = self.env['theme.utils']
        
        # Disable views first
        theme_utils.disable_view('website.template_header_default')
        theme_utils.disable_view('website.template_footer_contact')
        
        # Call the method multiple times
        if self.theme_clean_module:
            theme_utils._theme_clean_post_copy(self.theme_clean_module)
            theme_utils._theme_clean_post_copy(self.theme_clean_module)
            theme_utils._theme_clean_post_copy(self.theme_clean_module)
        
        # Verify views are still enabled (should not break on multiple calls)
        header_view = self.ir_ui_view.search([
            ('key', '=', 'website.template_header_default')
        ], limit=1)
        footer_view = self.ir_ui_view.search([
            ('key', '=', 'website.template_footer_contact')
        ], limit=1)
        
        if header_view:
            self.assertTrue(
                header_view.active,
                "Header view should remain enabled after multiple calls"
            )
        if footer_view:
            self.assertTrue(
                footer_view.active,
                "Footer view should remain enabled after multiple calls"
            )

    def test_08_enable_view_method_works(self):
        """Test that enable_view method works correctly"""
        theme_utils = self.env['theme.utils']
        
        # Test enabling a view
        theme_utils.enable_view('website.template_header_default')
        
        header_view = self.ir_ui_view.search([
            ('key', '=', 'website.template_header_default')
        ], limit=1)
        
        if header_view:
            self.assertTrue(
                header_view.active,
                "enable_view should activate the view"
            )

    def test_09_disable_view_method_works(self):
        """Test that disable_view method works correctly"""
        theme_utils = self.env['theme.utils']
        
        # First enable the view
        theme_utils.enable_view('website.template_header_default')
        
        # Then disable it
        theme_utils.disable_view('website.template_header_default')
        
        header_view = self.ir_ui_view.search([
            ('key', '=', 'website.template_header_default')
        ], limit=1)
        
        if header_view:
            self.assertFalse(
                header_view.active,
                "disable_view should deactivate the view"
            )

    def test_10_theme_clean_module_installed(self):
        """Test that theme_clean module can be found"""
        self.assertTrue(
            self.theme_clean_module,
            "theme_clean module should exist in the system"
        )
        
        if self.theme_clean_module:
            self.assertEqual(
                self.theme_clean_module.name,
                'theme_clean',
                "Module name should be 'theme_clean'"
            )


# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import TransactionCase, tagged


@tagged('post_install', '-at_install')
class TestThemeCommon(TransactionCase):
    """Test cases for theme_common module"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.theme_utils = cls.env['theme.utils']
        cls.ir_module_module = cls.env['ir.module.module']
        cls.theme_ir_asset = cls.env['theme.ir.asset']
        
        # Get the theme_common module
        cls.theme_common_module = cls.ir_module_module.search([
            ('name', '=', 'theme_common')
        ], limit=1)
        
        # Ensure website module is installed (required for theme.utils)
        cls.website_module = cls.ir_module_module.search([
            ('name', '=', 'website')
        ], limit=1)
        if cls.website_module.state != 'installed':
            cls.website_module.button_immediate_install()
        
        # List of color option assets that should be disabled
        cls.color_option_assets = [
            'theme_common.option_colors_02_variables',
            'theme_common.option_colors_03_variables',
            'theme_common.option_colors_04_variables',
            'theme_common.option_colors_05_variables',
            'theme_common.option_colors_06_variables',
            'theme_common.option_colors_07_variables',
            'theme_common.option_colors_08_variables',
        ]

    def test_01_theme_common_model_exists(self):
        """Test that ThemeCommon model exists and inherits from theme.utils"""
        self.assertTrue(
            self.env['theme.utils']._name == 'theme.utils',
            "theme.utils model should exist"
        )
        
        # Check that theme_common module provides ThemeCommon model
        theme_common_model = self.env['theme.utils']
        self.assertTrue(
            hasattr(theme_common_model, '_theme_common_post_copy'),
            "ThemeCommon model should have _theme_common_post_copy method"
        )

    def test_02_theme_common_post_copy_method_exists(self):
        """Test that _theme_common_post_copy method exists and is callable"""
        theme_utils = self.env['theme.utils']
        
        # Check method exists
        self.assertTrue(
            hasattr(theme_utils, '_theme_common_post_copy'),
            "_theme_common_post_copy method should exist"
        )
        
        # Check it's callable
        self.assertTrue(
            callable(getattr(theme_utils, '_theme_common_post_copy', None)),
            "_theme_common_post_copy should be callable"
        )

    def test_03_theme_common_post_copy_disables_all_color_options(self):
        """Test that _theme_common_post_copy disables all 7 color option assets"""
        theme_utils = self.env['theme.utils']
        
        # Enable all color option assets first
        for asset_key in self.color_option_assets:
            theme_utils.enable_asset(asset_key)
        
        # Verify all assets are enabled
        for asset_key in self.color_option_assets:
            asset = self.theme_ir_asset.search([
                ('key', '=', asset_key)
            ], limit=1)
            if asset:
                self.assertTrue(
                    asset.active,
                    f"Asset {asset_key} should be enabled before test"
                )
        
        # Call the method
        if self.theme_common_module:
            theme_utils._theme_common_post_copy(self.theme_common_module)
        
        # Verify all assets are disabled
        for asset_key in self.color_option_assets:
            asset = self.theme_ir_asset.search([
                ('key', '=', asset_key)
            ], limit=1)
            if asset:
                self.assertFalse(
                    asset.active,
                    f"Asset {asset_key} should be disabled after _theme_common_post_copy"
                )

    def test_04_theme_common_post_copy_disables_option_colors_02(self):
        """Test that _theme_common_post_copy disables option_colors_02_variables"""
        theme_utils = self.env['theme.utils']
        asset_key = 'theme_common.option_colors_02_variables'
        
        # Enable the asset first
        theme_utils.enable_asset(asset_key)
        
        # Verify asset is enabled
        asset = self.theme_ir_asset.search([
            ('key', '=', asset_key)
        ], limit=1)
        if asset:
            self.assertTrue(
                asset.active,
                "Asset should be enabled before test"
            )
        
        # Call the method
        if self.theme_common_module:
            theme_utils._theme_common_post_copy(self.theme_common_module)
        
        # Verify asset is disabled
        asset = self.theme_ir_asset.search([
            ('key', '=', asset_key)
        ], limit=1)
        if asset:
            self.assertFalse(
                asset.active,
                "Asset should be disabled after _theme_common_post_copy"
            )

    def test_05_theme_common_post_copy_disables_option_colors_03(self):
        """Test that _theme_common_post_copy disables option_colors_03_variables"""
        theme_utils = self.env['theme.utils']
        asset_key = 'theme_common.option_colors_03_variables'
        
        # Enable the asset first
        theme_utils.enable_asset(asset_key)
        
        # Call the method
        if self.theme_common_module:
            theme_utils._theme_common_post_copy(self.theme_common_module)
        
        # Verify asset is disabled
        asset = self.theme_ir_asset.search([
            ('key', '=', asset_key)
        ], limit=1)
        if asset:
            self.assertFalse(
                asset.active,
                "Asset should be disabled after _theme_common_post_copy"
            )

    def test_06_theme_common_post_copy_disables_option_colors_04(self):
        """Test that _theme_common_post_copy disables option_colors_04_variables"""
        theme_utils = self.env['theme.utils']
        asset_key = 'theme_common.option_colors_04_variables'
        
        # Enable the asset first
        theme_utils.enable_asset(asset_key)
        
        # Call the method
        if self.theme_common_module:
            theme_utils._theme_common_post_copy(self.theme_common_module)
        
        # Verify asset is disabled
        asset = self.theme_ir_asset.search([
            ('key', '=', asset_key)
        ], limit=1)
        if asset:
            self.assertFalse(
                asset.active,
                "Asset should be disabled after _theme_common_post_copy"
            )

    def test_07_theme_common_post_copy_disables_option_colors_05(self):
        """Test that _theme_common_post_copy disables option_colors_05_variables"""
        theme_utils = self.env['theme.utils']
        asset_key = 'theme_common.option_colors_05_variables'
        
        # Enable the asset first
        theme_utils.enable_asset(asset_key)
        
        # Call the method
        if self.theme_common_module:
            theme_utils._theme_common_post_copy(self.theme_common_module)
        
        # Verify asset is disabled
        asset = self.theme_ir_asset.search([
            ('key', '=', asset_key)
        ], limit=1)
        if asset:
            self.assertFalse(
                asset.active,
                "Asset should be disabled after _theme_common_post_copy"
            )

    def test_08_theme_common_post_copy_disables_option_colors_06(self):
        """Test that _theme_common_post_copy disables option_colors_06_variables"""
        theme_utils = self.env['theme.utils']
        asset_key = 'theme_common.option_colors_06_variables'
        
        # Enable the asset first
        theme_utils.enable_asset(asset_key)
        
        # Call the method
        if self.theme_common_module:
            theme_utils._theme_common_post_copy(self.theme_common_module)
        
        # Verify asset is disabled
        asset = self.theme_ir_asset.search([
            ('key', '=', asset_key)
        ], limit=1)
        if asset:
            self.assertFalse(
                asset.active,
                "Asset should be disabled after _theme_common_post_copy"
            )

    def test_09_theme_common_post_copy_disables_option_colors_07(self):
        """Test that _theme_common_post_copy disables option_colors_07_variables"""
        theme_utils = self.env['theme.utils']
        asset_key = 'theme_common.option_colors_07_variables'
        
        # Enable the asset first
        theme_utils.enable_asset(asset_key)
        
        # Call the method
        if self.theme_common_module:
            theme_utils._theme_common_post_copy(self.theme_common_module)
        
        # Verify asset is disabled
        asset = self.theme_ir_asset.search([
            ('key', '=', asset_key)
        ], limit=1)
        if asset:
            self.assertFalse(
                asset.active,
                "Asset should be disabled after _theme_common_post_copy"
            )

    def test_10_theme_common_post_copy_disables_option_colors_08(self):
        """Test that _theme_common_post_copy disables option_colors_08_variables"""
        theme_utils = self.env['theme.utils']
        asset_key = 'theme_common.option_colors_08_variables'
        
        # Enable the asset first
        theme_utils.enable_asset(asset_key)
        
        # Call the method
        if self.theme_common_module:
            theme_utils._theme_common_post_copy(self.theme_common_module)
        
        # Verify asset is disabled
        asset = self.theme_ir_asset.search([
            ('key', '=', asset_key)
        ], limit=1)
        if asset:
            self.assertFalse(
                asset.active,
                "Asset should be disabled after _theme_common_post_copy"
            )

    def test_11_theme_common_post_copy_with_none_module(self):
        """Test that _theme_common_post_copy handles None module parameter gracefully"""
        theme_utils = self.env['theme.utils']
        
        # Should not raise an error even with None
        try:
            theme_utils._theme_common_post_copy(None)
        except Exception as e:
            self.fail(
                f"_theme_common_post_copy should handle None module gracefully, "
                f"but raised {type(e).__name__}: {e}"
            )

    def test_12_theme_common_post_copy_idempotent(self):
        """Test that calling _theme_common_post_copy multiple times is idempotent"""
        theme_utils = self.env['theme.utils']
        
        # Enable all assets first
        for asset_key in self.color_option_assets:
            theme_utils.enable_asset(asset_key)
        
        # Call the method multiple times
        if self.theme_common_module:
            theme_utils._theme_common_post_copy(self.theme_common_module)
            theme_utils._theme_common_post_copy(self.theme_common_module)
            theme_utils._theme_common_post_copy(self.theme_common_module)
        
        # Verify all assets are still disabled (should not break on multiple calls)
        for asset_key in self.color_option_assets:
            asset = self.theme_ir_asset.search([
                ('key', '=', asset_key)
            ], limit=1)
            if asset:
                self.assertFalse(
                    asset.active,
                    f"Asset {asset_key} should remain disabled after multiple calls"
                )

    def test_13_theme_common_post_copy_does_not_affect_other_assets(self):
        """Test that _theme_common_post_copy only affects the 7 color option assets"""
        theme_utils = self.env['theme.utils']
        
        # Enable a different asset (not in the color options list)
        other_asset_key = 'theme_common.primary_variables_scss'
        theme_utils.enable_asset(other_asset_key)
        
        # Call the method
        if self.theme_common_module:
            theme_utils._theme_common_post_copy(self.theme_common_module)
        
        # Verify the other asset is still enabled (not affected)
        other_asset = self.theme_ir_asset.search([
            ('key', '=', other_asset_key)
        ], limit=1)
        if other_asset:
            self.assertTrue(
                other_asset.active,
                "Other assets should not be affected by _theme_common_post_copy"
            )

    def test_14_enable_asset_method_works(self):
        """Test that enable_asset method works correctly"""
        theme_utils = self.env['theme.utils']
        asset_key = 'theme_common.option_colors_02_variables'
        
        # Disable the asset first
        theme_utils.disable_asset(asset_key)
        
        # Then enable it
        theme_utils.enable_asset(asset_key)
        
        asset = self.theme_ir_asset.search([
            ('key', '=', asset_key)
        ], limit=1)
        
        if asset:
            self.assertTrue(
                asset.active,
                "enable_asset should activate the asset"
            )

    def test_15_disable_asset_method_works(self):
        """Test that disable_asset method works correctly"""
        theme_utils = self.env['theme.utils']
        asset_key = 'theme_common.option_colors_02_variables'
        
        # First enable the asset
        theme_utils.enable_asset(asset_key)
        
        # Then disable it
        theme_utils.disable_asset(asset_key)
        
        asset = self.theme_ir_asset.search([
            ('key', '=', asset_key)
        ], limit=1)
        
        if asset:
            self.assertFalse(
                asset.active,
                "disable_asset should deactivate the asset"
            )

    def test_16_theme_common_module_installed(self):
        """Test that theme_common module can be found"""
        self.assertTrue(
            self.theme_common_module,
            "theme_common module should exist in the system"
        )
        
        if self.theme_common_module:
            self.assertEqual(
                self.theme_common_module.name,
                'theme_common',
                "Module name should be 'theme_common'"
            )

    def test_17_color_option_assets_exist(self):
        """Test that all 7 color option assets exist in the system"""
        for asset_key in self.color_option_assets:
            asset = self.theme_ir_asset.search([
                ('key', '=', asset_key)
            ], limit=1)
            self.assertTrue(
                asset,
                f"Color option asset {asset_key} should exist in the system"
            )

    def test_18_theme_common_post_copy_resets_default_colors(self):
        """Test that _theme_common_post_copy resets default colors as documented"""
        theme_utils = self.env['theme.utils']
        
        # Enable all color options to simulate a previous theme with colors
        for asset_key in self.color_option_assets:
            theme_utils.enable_asset(asset_key)
        
        # Call the method (should reset all default colors)
        if self.theme_common_module:
            theme_utils._theme_common_post_copy(self.theme_common_module)
        
        # Verify all color options are disabled (reset)
        for asset_key in self.color_option_assets:
            asset = self.theme_ir_asset.search([
                ('key', '=', asset_key)
            ], limit=1)
            if asset:
                self.assertFalse(
                    asset.active,
                    f"Color option {asset_key} should be reset (disabled) when switching themes"
                )


# test_glowprism.py
"""
Tests for GlowPrism module.
"""

import unittest
from glowprism import GlowPrism

class TestGlowPrism(unittest.TestCase):
    """Test cases for GlowPrism class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GlowPrism()
        self.assertIsInstance(instance, GlowPrism)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GlowPrism()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

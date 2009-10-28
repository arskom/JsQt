
# http://codespeak.net/lxml/tutorial.html

# the ultra-portable etree import

import jsqt

try:
    from lxml import etree
    jsqt.debug_print("running with lxml.etree")
except ImportError:
    try: # Python 2.5+
        import xml.etree.cElementTree as etree
        jsqt.debug_print("running with cElementTree on Python 2.5+")
    except ImportError:
        try: # Python 2.5+
            import xml.etree.ElementTree as etree
            jsqt.debug_print("running with ElementTree on Python 2.5+")
        except ImportError:
            try: # normal cElementTree install
                import cElementTree as etree
                jsqt.debug_print("running with cElementTree")
            except ImportError:
                try: # normal ElementTree install
                    import elementtree.ElementTree as etree
                    jsqt.debug_print("running with ElementTree")
                except ImportError:
                    jsqt.debug_print("Failed to import ElementTree from any known place")

# http://codespeak.net/lxml/tutorial.html

# the ultra-portable etree import
try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
    try: # Python 2.5+
        import xml.etree.cElementTree as etree
        print("running with cElementTree on Python 2.5+")
    except ImportError:
        try: # Python 2.5+
            import xml.etree.ElementTree as etree
            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try: # normal cElementTree install
                import cElementTree as etree
                print("running with cElementTree")
            except ImportError:
                try: # normal ElementTree install
                    import elementtree.ElementTree as etree
                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")
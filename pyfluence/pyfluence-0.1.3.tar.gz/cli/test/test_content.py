from cement.utils import test
from cli.main import PyfluenceApp

class TestContentController(test.CementTestCase):
    app_class = PyfluenceApp

    def setUp(self):
        super(TestContentController, self).setUp()

    def test_add_change_delete(self):

        self.add_app = self.app_class(argv=
                                  ["content",
                                   "add",
                                   "--content_title", "Test 1",
                                   "--space", "TEST",
                                   "--content_type", "page",
                                   "--content_file", "/Users/karim/dev/tools/pyfluence/pyfluence/tests/data/content.html"
                                   ], config_files=[])


        self.ok(app.config.has_key('myapp', 'debug'))
        self.eq(app.config.get('myapp', 'debug'), False)

        # Run the applicaion, if necessary
        app.run()

        # Test the last rendered output (if app.render was used)
        data, output = app.get_last_rendered()
        self.eq(data, {'foo':'bar'})
        self.eq(output, 'some rendered output text')

    @test.raises(Exception)
    def test_exception(self):
        try:
            # Perform tests that intentionally cause an exception.  The
            # test passes only if the exception is raised.
            raise Exception('test')
        except Exception as e:
            # Do further checks to ensure the proper exception was raised
            self.eq(e.args[0], 'Some Exception Message')

            # Finally, call raise again which re-raises the exception that
            # we just caught.  This completes our test (to actually
            # verify that the exception was raised)
            raise
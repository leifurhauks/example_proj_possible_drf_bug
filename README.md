When I run `./manage.py test` in the `proj` directory, I get the following output:

    Creating test database for alias 'default'...
    F.F.
    ======================================================================
    FAIL: test_profile_create_view (profiles.tests.ProfileTests)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/home/leifur/code/example_proj_possible_drf_bug/proj/profiles/tests.py", line 35, in test_profile_create_view
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
    AssertionError: 400 != 201 : {'tags': ['This list may not be empty.']}
    
    ======================================================================
    FAIL: test_serializer_with_querydict (profiles.tests.ProfileTests)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/home/leifur/code/example_proj_possible_drf_bug/proj/profiles/tests.py", line 51, in test_serializer_with_querydict
        self.assertTrue(serializer.is_valid(), serializer.errors)
    AssertionError: False is not true : {'tags': ['This list may not be empty.']}
    
    ----------------------------------------------------------------------
    Ran 4 tests in 0.010s
    
    FAILED (failures=2)
    Destroying test database for alias 'default'...



import inspect
import time

from ajunit.debugjunkie import LogJunkie
from ajunit.decorators import DecoratorType


class TestJunkieExecutionError(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)


class TestListenerError(TestJunkieExecutionError):

    def __init__(self, message):
        TestJunkieExecutionError.__init__(self, message)


class ConfigError(TestJunkieExecutionError):

    def __init__(self, message):
        TestJunkieExecutionError.__init__(self, message)


class TestCategories:

    SUCCESS = "success"
    FAIL = "fail"
    IGNORE = "ignore"
    ERROR = "error"
    SKIP = "skip"
    ALL = [SUCCESS, FAIL, IGNORE, ERROR, SKIP]
    ALL_UN_SUCCESSFUL = [FAIL, IGNORE, ERROR, SKIP]


class TestRunner:

    __STATS = {}

    def __init__(self):

        pass

    def __update_class_stats(self):

        pass

    @staticmethod
    def __update_stats(class_object, test_function, param, error, start_time, category, class_retry_attempt):
        string_param = str(param)
        performance = time.time() - start_time

        def __previous_stats():
            __stats = {"retries": 0, "exceptions": [], "performance": []}
            if class_object in TestRunner.__STATS:
                for _category in TestCategories.ALL:
                    if _category in TestRunner.__STATS[class_object]:
                        if test_function in TestRunner.__STATS[class_object][_category]:
                            if string_param in TestRunner.__STATS[class_object][_category][test_function]:
                                _test_stats = TestRunner.__STATS[class_object][_category][test_function][string_param]
                                __stats.update({"retries": _test_stats.get("retries", 0)})
                                __stats.update({"exceptions": _test_stats.get("exceptions", [])})
                                __stats.update({"performance": _test_stats.get("performance", [])})
                                break
            return __stats

        def __remove_from_previous_category():
            for _category in TestRunner.__STATS[class_object]:
                if _category != category and _category in TestCategories.ALL:
                    if test_function in TestRunner.__STATS[class_object][_category]:
                        if string_param in TestRunner.__STATS[class_object][_category][test_function]:
                            TestRunner.__STATS[class_object][_category][test_function].pop(string_param)
                            LogJunkie.debug("<< Test: {} Param: {} moved from: {} to: {} category"
                                            .format(test_function, string_param, _category, category))
                            if not TestRunner.__STATS[class_object][_category][test_function]:
                                TestRunner.__STATS[class_object][_category].pop(test_function)
                                LogJunkie.debug("<< Removed: {} from category: {}, no other parameters have failed."
                                                .format(test_function, _category))

        previous_stats = __previous_stats()
        retries = previous_stats["retries"] + 1
        errors = previous_stats["exceptions"] + [error]
        performance = previous_stats["performance"] + [performance]
        properties = {string_param: {"retries": retries,
                                     "exceptions": errors,
                                     "performance": performance,
                                     "parameter": param}}
        updated_stats = {test_function: properties}
        LogJunkie.debug("<< Updated Stats: {}".format(updated_stats))
        if class_object not in TestRunner.__STATS:
            TestRunner.__STATS.update({class_object: {category: updated_stats}})
        elif category not in TestRunner.__STATS[class_object]:
            TestRunner.__STATS[class_object].update({category: updated_stats})
        elif test_function not in TestRunner.__STATS[class_object][category]:
            TestRunner.__STATS[class_object][category].update(updated_stats)
        else:
            TestRunner.__STATS[class_object][category][test_function].update(properties)
        TestRunner.__STATS[class_object]["class_retried"] = class_retry_attempt

        __remove_from_previous_category()

    @staticmethod
    def get_stats():
        from ajunit.statsjunkie import StatsJunkie
        return StatsJunkie(TestRunner.__STATS)

    @staticmethod
    def __get_stats():
        return TestRunner.__STATS

    @staticmethod
    def run(suite_provider, **kwargs):
        start_time = time.time()
        from ajunit.suitebuilder import SuiteBuilder
        if not isinstance(suite_provider, list):
            suite_provider = [suite_provider]

        for request in suite_provider:
            suite_object = SuiteBuilder.get_execution_roster().get(request, None)
            if suite_object is not None:
                TestRunner.__process_decorators(suite_object, **kwargs)
        print("--- done in {} seconds ---".format(time.time() - start_time))
        print("--- {}/{} ---".format(TestRunner.get_stats().get_total_test_count() -
                                     TestRunner.get_stats().get_unsuccessful_test_count(),
                                     TestRunner.get_stats().get_total_test_count()))

    @staticmethod
    def __default_processor(suite_object, decorator_type):

        functions_list = suite_object["suite_definition"].get(decorator_type)
        for func in functions_list:
            start_time = time.time()
            try:
                func["decorated_function"](func["decorated_function"])
            except Exception as error:
                raise error
            finally:
                if suite_object["class_object"] not in TestRunner.__STATS:
                    TestRunner.__STATS.update({
                        suite_object["class_object"]: {"class_performance": {decorator_type: [time.time() -
                                                                                              start_time]}}})
                elif decorator_type not in TestRunner.__STATS[suite_object["class_object"]]["class_performance"]:
                    TestRunner.__STATS[suite_object["class_object"]]["class_performance"].update({
                        decorator_type: [time.time() - start_time]})
                else:
                    TestRunner.__STATS[suite_object["class_object"]]["class_performance"][decorator_type].append(
                        time.time() - start_time)

    @staticmethod
    def __execute_test(suite_object, decorated_function, suite_listener,
                       retry_attempts, class_retry_attempt, parameter=None, before_class_error=None):
        start_time = time.time()
        if before_class_error is not None:
            TestRunner.__update_stats(class_object=suite_object["class_object"],
                                      test_function=decorated_function,
                                      param=parameter,
                                      error=before_class_error,
                                      start_time=start_time,
                                      category=TestCategories.IGNORE,
                                      class_retry_attempt=class_retry_attempt)
            TestRunner.__process_event_listener(suite_listener.on_ignore, error=before_class_error)
            return
        try:
            for retry_attempt in range(1, retry_attempts + 1):
                LogJunkie.debug(">> Test Case: {} Param: {} Retry Attempt: {}/{}"
                                .format(decorated_function, parameter, retry_attempt, retry_attempts))
                try:
                    TestRunner.__default_processor(suite_object=suite_object,
                                                   decorator_type=DecoratorType.BEFORE_TEST)
                    if "parameter" in inspect.getargspec(decorated_function).args:  # deprecated but supports Python 2
                        decorated_function(decorated_function, parameter=parameter)
                    else:
                        decorated_function(decorated_function)
                    TestRunner.__default_processor(suite_object=suite_object,
                                                   decorator_type=DecoratorType.AFTER_TEST)
                    TestRunner.__update_stats(class_object=suite_object["class_object"],
                                              test_function=decorated_function,
                                              param=parameter,
                                              error=None,
                                              start_time=start_time,
                                              category=TestCategories.SUCCESS,
                                              class_retry_attempt=class_retry_attempt)
                    TestRunner.__process_event_listener(suite_listener.on_success)
                    return
                except Exception as error:
                    if not isinstance(error, TestJunkieExecutionError):
                        LogJunkie.print_traceback()
                        if retry_attempt == retry_attempts:
                            raise error
                        else:
                            TestRunner.__update_stats(class_object=suite_object["class_object"],
                                                      test_function=decorated_function,
                                                      param=parameter,
                                                      error=error,
                                                      start_time=start_time,
                                                      category=TestCategories.FAIL if isinstance(error, AssertionError)
                                                      else TestCategories.ERROR,
                                                      class_retry_attempt=class_retry_attempt)
                    else:
                        raise error
        except Exception as error:
            if not isinstance(error, TestJunkieExecutionError):
                LogJunkie.print_traceback()
                __category = TestCategories.ERROR
                __event = suite_listener.on_error
                if isinstance(error, AssertionError):
                    __category = TestCategories.FAIL
                    __event = suite_listener.on_failure
                TestRunner.__update_stats(class_object=suite_object["class_object"],
                                          test_function=decorated_function,
                                          param=parameter,
                                          error=error,
                                          start_time=start_time,
                                          category=__category,
                                          class_retry_attempt=class_retry_attempt)
                TestRunner.__process_event_listener(__event, error=error)
            else:
                raise error

    @staticmethod
    def __process_event_listener(event_function, error=None):
        try:
            if error is not None:
                event_function(error)
            else:
                event_function()
        except Exception:
            LogJunkie.print_traceback()
            raise TestListenerError("Exception occurred while processing custom event listener with: {}"
                                    .format(event_function))

    @staticmethod
    def __runnable_tags(test_tags, tag_config):

        if not test_tags and tag_config is not None:
            # tests without tags will be skipped if tags were provided to the runner
            return False

        if tag_config is not None:
            try:
                if tag_config.get("skip_on_match_all", None) is not None:
                    for tag in tag_config["skip_on_match_all"]:
                        if tag not in test_tags:
                            return True
                    return False
                elif tag_config.get("skip_on_match_any", None) is not None:
                    for tag in tag_config["skip_on_match_any"]:
                        if tag in test_tags:
                            return False
                elif tag_config.get("run_on_match_all", None) is not None:
                    for tag in tag_config["run_on_match_all"]:
                        if tag not in test_tags:
                            return False
                elif tag_config.get("run_on_match_any", None) is not None:
                    for tag in tag_config["run_on_match_any"]:
                        if tag in test_tags:
                            return True
                    return False
                else:
                    raise ConfigError("Incorrect configuration is set for `tag_config`")
            except Exception as error:
                if not isinstance(error, ConfigError):
                    raise ConfigError("Failed to parse `tag_config`. Make sure tags are provided as a list")
                raise error
        return True

    @staticmethod
    def __process_decorators(suite_object, **kwargs):

        suite_definition = suite_object["suite_definition"]
        suite_listener = suite_object["test_listener"](class_meta=suite_object["class_meta"])
        suite_retry_attempts = suite_object.get("class_retry", 1)
        suite_skip = suite_object.get("class_skip", False)
        test_objects = suite_definition.get(DecoratorType.TEST_CASE)
        before_class_error = None
        unsuccessful_tests = None
        if not suite_skip:
            for suite_retry_attempt in range(1, suite_retry_attempts + 1):
                if suite_retry_attempt == 1 or TestRunner.__get_unsuccessful_tests(suite_object["class_object"]):
                    LogJunkie.debug("Running suite: {}".format(suite_object["class_object"]))
                    LogJunkie.debug("Suite Retry {}/{}".format(suite_retry_attempt, suite_retry_attempts))
                    try:
                        TestRunner.__default_processor(suite_object=suite_object,
                                                       decorator_type=DecoratorType.BEFORE_CLASS)
                    except Exception as error:
                        if isinstance(error, AssertionError):
                            TestRunner.__process_event_listener(suite_listener.on_before_class_failure, error=error)
                        else:
                            TestRunner.__process_event_listener(suite_listener.on_before_class_error, error=error)
                        before_class_error = error
                    if suite_retry_attempt > 1:
                        unsuccessful_tests = TestRunner.__get_unsuccessful_tests(suite_object["class_object"])
                        LogJunkie.debug("There are {} unsuccessful tests that will be retried"
                                        .format(len(unsuccessful_tests)))
                        if not unsuccessful_tests:
                            break
                    for test_object in test_objects:
                        start_time = time.time()

                        def __qualified_for_retry(_unsuccessful_tests, _decorated_function, _parameter=None):
                            def __post_qualified_msg():
                                LogJunkie.debug("Test: {} Param: {} Qualified for retry, it has failed before"
                                                .format(_decorated_function, _parameter))
                            for _unsuccessful_test in _unsuccessful_tests:
                                if isinstance(_unsuccessful_test, type(_decorated_function)):
                                    if _unsuccessful_test == _decorated_function:
                                        __post_qualified_msg()
                                        return True
                                elif _decorated_function in _unsuccessful_test:
                                    if isinstance(_unsuccessful_test, dict):
                                        if _unsuccessful_test[_decorated_function] == _parameter:
                                            __post_qualified_msg()
                                            return True
                                    else:
                                        __post_qualified_msg()
                                        return True
                            LogJunkie.debug("Test: {} Param: {} Not qualified for retry - Already successful"
                                            .format(_decorated_function, _parameter))
                            return False

                        decorated_function = test_object["decorated_function"]
                        decorator_kwargs = test_object["decorator_kwargs"]
                        retries = decorator_kwargs.get("retry", 1)
                        test_tags = decorator_kwargs.get("tags", [])
                        suite_listener.kwargs.update({"test_meta": decorator_kwargs})
                        suite_listener.kwargs.update({"test_junkie_meta": {"function_name": decorated_function.__name__}})

                        def __skip_condition():
                            val = decorator_kwargs.get("skip", False)
                            if inspect.isfunction(val):
                                try:
                                    if "meta" in inspect.getargspec(val).args:  # deprecated but supports Python 2
                                        val = val(meta=suite_listener.kwargs)
                                    val = val()
                                    assert isinstance(val, bool), "Function: {} must return a boolean. Got: {}"\
                                                                  .format(val, type(val))
                                except Exception:
                                    LogJunkie.print_traceback()
                                    raise TestJunkieExecutionError("Encountered error while processing skip condition")
                            return val

                        LogJunkie.debug("===============Running test: {}==================".format(decorated_function))
                        if not __skip_condition() and TestRunner.__runnable_tags(
                                test_tags=test_tags, tag_config=kwargs.get("tag_config", None)):
                            parameters = decorator_kwargs.get("parameters", [None])
                            if not parameters or not isinstance(parameters, list):
                                try:
                                    if isinstance(parameters, list):
                                        raise Exception("Empty parameters list in Class: {} Function: {}"
                                                        .format(suite_object["class_object"].__module__,
                                                                decorated_function.__name__))
                                    else:
                                        raise Exception("Wrong parameters data type. Expected: {} was: {} in Class: {} "
                                                        "Function: {}".format(list, type(parameters),
                                                                              suite_object["class_object"].__module__,
                                                                              decorated_function.__name__))
                                except Exception as error:
                                    LogJunkie.print_traceback()
                                    TestRunner.__update_stats(class_object=suite_object["class_object"],
                                                              test_function=decorated_function,
                                                              param=None,
                                                              error=error,
                                                              start_time=start_time,
                                                              category=TestCategories.IGNORE,
                                                              class_retry_attempt=suite_retry_attempt)
                                    TestRunner.__process_event_listener(suite_listener.on_ignore, error=error)
                            else:
                                for param in parameters:
                                    if unsuccessful_tests is not None:
                                        if not __qualified_for_retry(unsuccessful_tests, decorated_function, param):
                                            continue
                                    suite_listener.kwargs["test_junkie_meta"].update({"parameter": param})
                                    TestRunner.__execute_test(suite_object=suite_object,
                                                              decorated_function=decorated_function,
                                                              suite_listener=suite_listener,
                                                              retry_attempts=retries,
                                                              parameter=param,
                                                              before_class_error=before_class_error,
                                                              class_retry_attempt=suite_retry_attempt)
                        else:
                            TestRunner.__update_stats(class_object=suite_object["class_object"],
                                                      test_function=decorated_function,
                                                      param=None,
                                                      error=None,
                                                      start_time=start_time,
                                                      category=TestCategories.SKIP,
                                                      class_retry_attempt=suite_retry_attempt)
                            TestRunner.__process_event_listener(suite_listener.on_skip)
                    try:
                        TestRunner.__default_processor(suite_object=suite_object,
                                                       decorator_type=DecoratorType.AFTER_CLASS)
                    except Exception as error:
                        if isinstance(error, AssertionError):
                            TestRunner.__process_event_listener(suite_listener.on_after_class_failure, error=error)
                        else:
                            TestRunner.__process_event_listener(suite_listener.on_after_class_error, error=error)
        else:
            TestRunner.__process_event_listener(suite_listener.on_class_skip)

    @staticmethod
    def __get_unsuccessful_tests(class_object):
        unsuccessful_tests = []
        executed_tests = TestRunner.__get_stats().get(class_object, [])
        for category in executed_tests:
            if category in TestCategories.ALL_UN_SUCCESSFUL:
                for test in executed_tests[category]:
                    for string_param, stats in executed_tests[category][test].items():
                        unsuccessful_tests.append({test: stats["parameter"]})
        return unsuccessful_tests

# TODO Place start_time in appropriate locations

from robot.api.deco import keyword


class GermaniumLocators:
    @keyword
    def find_element(self, what: str):
        from robot.running.namespace import IMPORTER
        selenium_library = find_library(IMPORTER, "SeleniumLibrary")
        wd = selenium_library.get_instance(create=False).driver

        raise AssertionError("not implemented")

    @staticmethod
    def noop():
        """
        Method so the optimizing imports aren't removing it
        :return:
        """
        pass


def find_library(importer, library_name: str):
    for library in importer._library_cache.values():
        if library.name == library_name:
            return library

    raise Exception(f"Unable to find {library_name}. Make sure you load the library.")

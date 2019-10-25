"""module with base class for test cases"""

from abc import abstractmethod


class BaseCase:
    """ Params:
            tc_id -test case id
            name - test case name
        methods:
            execute - execute test case
        abstract methods:
            prep - prepare for test case
                return:
                    "ok" - can run test case
                    raise exception - test case not run
            run - execute test case
                return:
                    result - test case result 
            clean_up - clean app after test case
                return:
                    'ok' - ok
    """

    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name

    def execute(self):
        """
        return:
            True - test passes
            False or raise exception - test fail
        """

        print(f"start executing tc_id: {self.tc_id}, name: {self.name}.")
        success = False
        try:
            m = self.prep()
        except Exception as e:
            print(e)
            print("test fail on prepare")
            return success
        else:
            print(f"prep success: {m}")
        try:
            result = self.run()
        except Exception as e:
            print(e)
        else:
            print(f"run success. result: {result}")
        try:
            m = self.clean_up()
        except Exception as e:
            print(e)
            return success
        else:
            print(f"clean up success: {m}")
            print(f"execute complete tc_id: {self.tc_id}, name: {self.name}.")
            success = True
            return success

    @abstractmethod
    def prep(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def clean_up(self):
        pass

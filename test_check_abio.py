import pytest
import paramiko
import sys
import logging
from Utilities.BaseClass import BaseClass


logger = logging.getLogger(__name__)


class TestAbio(BaseClass) :

    def test_check_ABIO(self):

        logger.info("infos")
        logger.warning("warnings")
        logger.error("errors")
        logger.critical("Critical")

        output = "empty"

        stdin, stdout, stderr = self.client.exec_command('chk adet')

        stdout = stdout.readlines()

        for line in stdout:
            output = output + line

        assert output != ""

        assert "failed : 0" in output, "ABIO not ready"

        if "failed : 0" in output:
            print("ABIO is ready")

        with open("ABIO_status.txt", "w") as ABIO_status:
            ABIO_status.write(output)

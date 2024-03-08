import pytest
import sys
sys.path.append("..")

import yaml
import datetime

from service.service import Service

@pytest.fixture
def service_class_instance():
    service = Service()
    with open("configs/testing-config.yml", 'r') as yaml_file:
            service.config = yaml.safe_load(yaml_file)

    # overwrite vertica_conn variables from config with the ones for local vertica db
    service.vertica_conn = service.config.get("conn_info")
    return service


@pytest.mark.filterwarnings("ignore")
def test_query_vertica(service_class_instance):
    results = service_class_instance.query_vertica("SELECT * FROM dims.dims_table WHERE month = 2")
    expected_results = [[2024, 2, 'Bs', datetime.date(2024, 2, 9)], [2024, 2, 'Sb', datetime.date(2024, 2, 9)]]
    assert results == expected_results